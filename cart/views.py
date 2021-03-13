from django.shortcuts import render, redirect
from items.models import Program, Lecture
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add the item to the cart to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    program = Program.objects.get(pk=item_id)
    lecture = Lecture.objects.get(pk=item_id)
    cart = request.session.get('cart', {})
    if request.POST:
        if item_id in list(cart.keys()):
            messages.error(
                request,
                'Item already in your cart!\
                Check your cart to continue purchase.')
            return redirect(redirect_url)
        else:
            cart[item_id] = quantity
            messages.success(request, 'Item was added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
