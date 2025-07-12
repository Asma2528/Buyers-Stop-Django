from django.db import models

#Stories model created for posting stories similar to products in shop app
class Stories(models.Model):
    blog_id=models.AutoField
    blog_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=6000)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="blog/images",default="")
#function for displaying blog name in our database
    def __str__(self):
        return self.blog_name
