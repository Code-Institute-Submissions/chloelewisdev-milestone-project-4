from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Rating(models.Model):
    """
    Enables users to add a product rating
    """
    rating = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating_title = models.CharField(max_length=200)
    rating_score = models.IntegerField(choices=rating)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating_title
