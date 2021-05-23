from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RatingForm
from .models import Rating, Product, UserProfile


@login_required
def add_rating(request):
    """
    Add a rating to a product
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rating successfully added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Rating failed, please ensure the form is\
                                    completed correctly.')
    else:
        form = RatingForm()

    template = 'ratings/add_rating.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
