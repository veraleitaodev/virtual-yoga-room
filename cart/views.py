from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from profiles.models import UserProfile
from items.models import Program

from .models import OrderItem, Order


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # filter products by id
    program = Program.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if program in request.user.profile.ebooks.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('products:product-list')) 
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('products:product-list'))

