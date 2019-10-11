from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.
#view for adding items into basket
@require_http_methods(["POST"])
def cart_add(request, product_id):
    cart =Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
        update_quantity=cd['update'])
    return redirect('cart:cart_detail')

#view for removing items

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

#view to display items in the cart
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True}) 
    return render(request, 'cart/detail.html', {'cart': cart})
