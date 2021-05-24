from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Rating
from .forms import RatingForm
from products.models import Product
from profiles.models import UserProfile



@login_required
def add_rating(request, product_id):
    """
    Add a rating to a product
    """
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_title = form.cleaned_data['rating_title']
            rating_description = form.cleaned_data['rating_description']
            rating_score = form.cleaned_data['rating_score']
            Rating.objects.create(
                user=user,
                product=get_object_or_404(Product, pk=product_id),
                rating_title=rating_title,
                rating_description=rating_description,
                rating_score=rating_score,
            )
            messages.success(request, 'Successfully added rating')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Rating failed, please ensure the form is\
                                    completed correctly and try again.')
    else:
        form = RatingForm()
    template = 'ratings/add_rating.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)
