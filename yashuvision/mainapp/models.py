from django.db import models
#this file decides the schema desion of db
#any changes to this file must be followed by the command
#python manage.py makemigration' -> to generate required DDl statement to affect the DB
#and then
#python manage.py 'migrate' -> to use these statements to affect the DB


# Create your models here.
class Product(models.Model):
    #providing the object attributes for
    name = models.CharField(max_length = 200) #this forms a varchar col in the 'product' table name 'name
    price = models.PositiveIntegerField()#unsigned integer
    desc = models.TextField() #become lonf=g or medium text
    stock = models.PositiveIntegerField(default =1) #stock int Default 1

    # for the image field,sql stores only the relative path images,the actual will be stored
    #in the specified media aerver subfolder,in this case 'products'.rest of config is in settings.py
    pic = models.ImageField(upload_to ="products/",null = True)
    def __str__(self):
        return f"product :{self.name}"
    