from django.shortcuts import render, redirect
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
