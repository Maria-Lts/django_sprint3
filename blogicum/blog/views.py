from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Category


POST_LIST_LIMIT = 5


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )[:POST_LIST_LIMIT]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        category__is_published=True,
        is_published=True,
        pub_date__lte=timezone.now(),
        pk=pk)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category=category
    )
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
