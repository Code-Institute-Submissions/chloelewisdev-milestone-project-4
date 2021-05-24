from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'testimonial_title',
        'testimonial_description',
    )

    ordering = ('testimonial_title',)


admin.site.register(Testimonial, TestimonialAdmin)
