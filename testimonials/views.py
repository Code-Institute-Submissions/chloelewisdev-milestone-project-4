from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Testimonial
from .forms import TestimonialForm


def testimonials(request):
    """
    A view to show all testimonials
    """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


@login_required
def add_testimonial(request):
    """
    A view for users with a profile to add
    a testimonial to the testimonials page
    """
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your testimonial\
                                      has been added successfully!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to add testimonial.\
                                    Please ensure the form is valid.')
    else:
        form = TestimonialForm
    
    form = TestimonialForm
    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
