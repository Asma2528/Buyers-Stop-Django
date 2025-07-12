from django.shortcuts import render #,redirect
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
from math import ceil
import json

#index function - main page of our site
def index(request):
        # products-all products list will be created 
        products= Product.objects.all()
        allProds=[]
        #catprods - list of dictionary{category and id}
        catprods= Product.objects.values('category', 'id')
        #cats - set of category
        cats= {item["category"] for item in catprods}
        for cat in cats:
            prod=Product.objects.filter(category=cat)
            n = len(prod)
            #logic for displaying products according to category in cards
            nSlide = n // 4 + ceil((n / 4) - (n // 4))
            #list of product, range and nSlide
            allProds.append([prod, range(1, nSlide), nSlide])
            #params- dictionary of allProds
        #with the help of allProds dictionary items can be fetched and then their values can be used
        params={'allProds':allProds }
        return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    #takes contact us form values and passes the values to Contact model
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        #These values will be saved in the Contact model
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')

def tracker(request):
    #when the form credentials are proper it would be stored in orderId and email variables.
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
           # print(order)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                    # update - list of description and date of order
                    # print(updates)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
            #to recognize errors
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')


def search(request):
    return render(request, 'search.html')

def products(request, myid):
    # Fetches the product using the id and passes it to prodView template
    product = Product.objects.filter(id=myid)
    return render(request, 'prodView.html', {'product':product[0]})

def checkout(request):
    if request.method=="POST":
        #json stored in database
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        #details fetched from form will be stored in variables then passed to order model
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        #order id and order description will be stored in orderUpdate model
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        #for generating alert in checkout page if all credentials are properly stored
        thank = True
        #for displaying id in alert
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')

# def loginuser(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         #to check if user has entered correct credentials
#         user = authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#         # A backend authenticated the credentials
#             return redirect("/")
#         else:
#             # No backend authenticated the credentials
#             return render(request,'login.html')
#     return render(request,'login.html')

# def logoutuser(request):
#     logout(request)
#     return redirect('/')