from django.db import models
from django.utils import timezone


class OwnerBlog(models.Model):
    """
    Similar to a blog, a place where the owner \
    can add important info and thoughts
    """
    blog_title = models.CharField(max_length=254)
    blog_content = models.TextField(blank=True, null=True, default='')
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.blog_title
