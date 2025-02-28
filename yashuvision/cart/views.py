from django.shortcuts import render, redirect
from mainapp.models import Product
from .models import cartItem
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
#c- creating cart items
@login_required
def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)# fection the product object
    # when adding product to cart, we need to check if the same user has added the same product
    #to cart before, in the case, we will not create a new cart item, rather just increment
    # quantity

    cart_item, created = cartItem.objects.get_or_create(product = this_product, user =request.user)
    cart_item.quantity += 1
    cart_item.save() # save changes to sql througe update
    return redirect('view_cart')

    #r - read cartitems
@login_required
def viewcart(request):
    template = 'cart.html'
    cart_items = cartItem.objects.filter(user = request.user)
     #the above statement is ewuivalent to : SELECT * FROM cartitem WHERE user = < USER_ID >;
    total_price = sum(float(item.product.price)* item.quantity for item in cart_items)

    context = {
        'cart_items' : cart_items,
        'total_price' : total_price
     }
    return render(request, template, context) 


@login_required
def removeFromCart(request, cart_item_id):
    this_cart_item = cartItem.objects.get(id = cart_item_id)
    this_cart_item.delete()
    return redirect('view_cart')

@login_required
def add_quantity(request, cart_item_id):
    cart_item = get_object_or_404(cartItem, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    overall_total = sum(item.get_total_price() for item in cartItem.objects.filter(user=request.user))
    return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.get_total_price(), 'overall_total': overall_total})

@login_required
def remove_quantity(request, cart_item_id):
    cart_item = get_object_or_404(cartItem, id=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        overall_total = sum(item.get_total_price() for item in cartItem.objects.filter(user=request.user))
        return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.get_total_price(), 'overall_total': overall_total})
    else:
        cart_item.delete()
        overall_total = sum(item.get_total_price() for item in cartItem.objects.filter(user=request.user))
        return JsonResponse({'quantity': 0, 'total_price': 0, 'overall_total': overall_total})