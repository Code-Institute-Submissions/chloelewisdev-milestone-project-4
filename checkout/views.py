from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are no hampers in your bag at the moment")
        return redirect (reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IsQN3HE50wCf5LFHpbMwiJ4SOm1azlvFxGpPLEVdK3hNqDufFSOzbTFXqBra9J3bvFeG6AtN5ohZ6kGQLJkkcgG00nmni6UsI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
