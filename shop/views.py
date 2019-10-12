from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Category, Product
from cart.forms import CartAddProductForm

@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render (request, 'shop/product/list.html',{'category': category, 'categories': categories, 'products': products})

# @login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,  'cart_product_form': cart_product_form})

# @login_required
# def index(request, category_slug=None):
#     if request.method == 'GET':
#         category = None
#         categories = Category.objects.all()
#         products = Product.objects.filter(available=True)
#         if category_slug:
#             category = get_object_or_404(Category, slug=category_slug)
#             products = products.filter(category=category)
#         return render (request, 'shop/product/list.html',{'category': category, 'categories': categories, 'products': products})
    
#     if request.method == 'POST':
#         pass
#     #     todo_item = TodoItem()
#     #     todo_item.title = request.POST['title']
#     #     todo_item.description = request.POST['description']
#     #     todo_item.status = False
#     #     todo_item.user = request.user
#     #     todo_item.save()
#     #     return HttpResponseRedirect(reverse('todoapp:index'))

    # return HttpResponseBadRequest()


# @login_required
# def details(request, pk):
#     todo = get_object_or_404(TodoItem, pk=pk, user=request.user)

#     if request.method == 'GET':
#         context = {
#             'todo': todo
#         }
#         return render(request, 'shop/details.html', context)

#     if request.method == 'POST':
#         todo.title = request.POST['title']
#         todo.description = request.POST['description']
#         status = request.POST.getlist('status')
#         if len(status) > 0:
#             todo.status = True
#         else:
#             todo.status = False
#         todo.save()
#         return HttpResponseRedirect(reverse('shop:product_list'))

#     return HttpResponseBadRequest()