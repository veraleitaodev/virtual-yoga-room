
from django.shortcuts import render, redirect, HttpResponse
from items.models import Program
from django.contrib import messages


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the selected product/service to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        messages.error(request, 'Items already in your cart!\
                Check your cart to continue booking.')
    else:
        cart[item_id] = quantity
        messages.success(request, 'Item was added to your cart')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        cart = request.session.get('cart', {})
        print(cart)
        cart.pop(item_id)
        messages.info(request, ('Removed item from your cart'))

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
