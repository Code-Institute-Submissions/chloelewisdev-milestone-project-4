from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Rating(models.Model):
    """
    Enables users to add a product rating
    """
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_rating')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    SCORES = (
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5'),
    )

    rating_score = models.IntegerField(default=3)
    rating_title = models.CharField(max_length=254)
    rating_description = models.TextField(max_length=1000, null=False, blank=False, default='')

    def __str__(self):
        return self.rating_title
