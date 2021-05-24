from django.shortcuts import render

from .models import Testimonial


def testimonials(request):
    """
    A view to show all testimonials
    """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)