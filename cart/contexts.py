from django.shortcuts import get_object_or_404
from items.models import Program


def cart_contents(request):
    """ Makes the cart content available across the whole website """

    cart_items = []
    total = 0
    items_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        program = get_object_or_404(Program, pk=item_id)
        total += quantity * program.price
        items_count += quantity
        cart_items.append({
            'program': program,
            'item_id': item_id,
            'quantity': quantity
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'items_count': items_count,
    }

    return context
