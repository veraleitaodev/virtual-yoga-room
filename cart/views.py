from django.shortcuts import render, redirect, get_object_or_404
from items.models import Program, Lecture
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add the item to the cart to the cart """

    program = get_object_or_404(Program, pk=item_id)
    lecture = get_object_or_404(Lecture, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if program:
        if item_id in list(cart.keys()):
            messages.error(
                request,
                f'{program.name} already in your\
                    cart! Check your cart to continue purchase.')
            return redirect(redirect_url)
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {program.name} to your bag')

    else:
        if item_id in list(cart.keys()):
            messages.error(
                request,
                f'{lecture.name} already in your\
                     cart! Check your cart to continue purchase.')
            return redirect(redirect_url)

        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {lecture.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)
