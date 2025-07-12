from django.contrib import admin
from django.urls import path
from shop import views

#Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL, matching against path_info . Once one of the URL patterns matches, Django imports and calls the given view, which is a Python function (or a class-based view).
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"), #To check where the order items have reached
    path("search/", views.search, name="Search"),
# path('login/',views.loginuser,name="login"),
# path('logout/',views.logoutuser,name="logout"),
    #<int:id> - for displaying product id in url 
    path("products/<int:myid>", views.products, name="ProductView"), #To have a detailed information about the products
    path("checkout/", views.checkout, name="Checkout"), #To place orders
]