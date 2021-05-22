from django.shortcuts import render


def add_rating(request):
    """
    Add a star rating to a product
    """
    return render(request, 'ratings/add_rating.html')
