from django.db import models
# Create your models here.

#Product model which contains all information about a product
class Product(models.Model):
   #AutoField. An IntegerField that automatically increments according to available IDs. You usually won't need to use this directly; a primary key field will automatically be added to your model if you don't specify otherwise.
    product_id=models.AutoField
    #CharField is a string field, for small- to large-sized strings. It is like a string field in C/C+++. CharField is generally used for storing small strings like first name, last name, etc. To store larger text TextField is used
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
        #IntegerField is a integer number represented in Python by a int instance. This field is generally used to store integer numbers in the database
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    #DateField is a field that stores date, represented in Python by a datetime.date instance. As the name suggests, this field is used to store an object of date created in python. The default form widget for this field is a TextInput. The admin can add a JavaScript calendar and a shortcut for “Today” explicitly.
    pub_date=models.DateField()
    #ImageField is a FileField with uploads restricted to image formats only.  Before uploading files, one needs to specify a lot of settings so that file is securely saved and can be retrieved in a convenient manner.
    image= models.ImageField(upload_to="shop/images",default="")
#function for displaying product name in our database instead of product object(x)
    def __str__(self):
        return self.product_name
    
    #Contact model for storing information of Contact us form values 
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
#function for displaying customer's name in our database 
    def __str__(self):
        return self.name
    
    #Orders model for storing information about the orders made by the customer 
class Order(models.Model):
    #primary_key=True implies null=False and unique=True. Only one primary key is allowed on an object.
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=99)
    address=models.CharField(max_length=120)
    phone = models.CharField(max_length=111, default="")
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

#OrderUpdate model for customers to get an update of their order such as where did the products reached,etc
class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    #The auto_now_add will set the timezone.now() only when the instance is created.
    timestamp= models.DateField(auto_now_add= True)
    def __str__(self):
        return self.update_desc[0:25] + "..."