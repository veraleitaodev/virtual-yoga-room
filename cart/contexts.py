from django.shortcuts import get_object_or_404
from items.models import Program


def cart_objects(request):
    """ Makes the cart content available across the whole website """

    cart_items = []
    total = 0
    items_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            program = get_object_or_404(Program, pk=item_id)
            total += item_data * program.price
            items_count += item_data
            cart_items.append({
                'program': program,
                'item_id': item_id,
                'quantity': item_data
            })

    context = {
        'cart_items': cart_items,
        'total': total,
        'items_count': items_count,
    }

    return context
