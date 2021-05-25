from django.db import models
from profiles.models import UserProfile


class Testimonial(models.Model):
    """
    Allows users who have a profile to
    leave a testimonial about their experience
    """
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_testimonial'
    )
    testimonial_title = models.CharField(max_length=254)
    testimonial_content = models.TextField(blank=True, null=True, default='')
    created_by = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.testimonial_title
