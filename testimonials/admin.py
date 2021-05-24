from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'testimonial_title',
        'testimonial_content',
        'created_by',
    )

    ordering = ('testimonial_title',)


admin.site.register(Testimonial, TestimonialAdmin)
