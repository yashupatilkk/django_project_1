from django.db import models
#cartItem table will nhave two foregin keys
#11.product id
# Create your models here.
from mainapp.models import Product

#2.user id
from django.contrib.auth.models import User

#create your models here
#lets's model a cartItem

class cartItem(models.Model):
    #1. product to cartItem has  a one to many relationship, this represented by a foregin key constraint
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #above, the 'on_delete = models, 'CASCADE' will ensure that all cartitems are deleted when a related product
    #is deleted
    #2. user to cartitem has a one to many relationship,again represented by a foegine key constraint
    #here also, we ensure that a cartitem is deleted authamatically if delete from the website
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #3.Quantity of the specific item in catrt
    quantity = models.PositiveIntegerField(default=1)

    #4. data when the product was added to cart
    data_added = models.DateField(auto_now_add=True)

    #string representation of cartitem object
    def __str__(self):
        return f"product:{self.product.name} - count: {self.quantity}"

        #method to find total price of particular item in cart
    def get_total_price(self):
        return self.quantity * self.product.price
