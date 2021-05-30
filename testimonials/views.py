from django.shortcuts import render, redirect, reverse, get_object_or_404
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
            return redirect(reverse('testimonials',))
        else:
            messages.error(request, 'Failed to add testimonial.\
                                    Please ensure the form is valid.')
    else:
        form = TestimonialForm()

    form = TestimonialForm()
    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_testimonial(request, testimonial_id):
    """
    Enables superuser to edit a testimonial
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only Camper Hampers owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    if request.method == 'POST':
        form = TestimonialForm(
            request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated testimonial!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to update testimonial. \
                                     Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)
        messages.info(
            request, f'You are editing {testimonial.testimonial_title}')

    template = 'testimonials/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


@login_required
def delete_testimonial(request, testimonial_id):
    """
    Allows superuser to delete a testimonial
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only Camper Hampers owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial successfully deleted.')

    return redirect(reverse('testimonials'))
