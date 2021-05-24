from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import OwnerBlog
from .forms import BlogForm


def blog(request):
    """
    A view to show all blog posts
    """
    blog = OwnerBlog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def new_blog(request):
    """
    Allows owner to add new blog content
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Camper Hampers owners can do that.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your blog post\
                                    has been added successfully!')
            return redirect(reverse('blog',))
        else:
            messages.error(request, 'Failed to add blog post.\
                                Please ensure the form is valid.')
    else:
        form = BlogForm()

    form = BlogForm()
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """
    Enables superuser to edit a blog
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Camper Hampers owners can do that.')
        return redirect(reverse('blog'))

    blog = get_object_or_404(OwnerBlog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(
            request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to update blog post. \
                                     Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.blog_title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ 
    Allows superuser to delete a blog
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Camper Hampers owners can do that.')
        return redirect(reverse('blog'))

    blog = get_object_or_404(OwnerBlog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog post successfully deleted.')

    return redirect(reverse('blog'))
