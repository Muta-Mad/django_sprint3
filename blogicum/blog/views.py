from datetime import datetime as dt

from django.shortcuts import render, get_object_or_404

from .models import Post, Category

POSTS_PER_PAGE = 5


def posts():
    """Получаем актуальные посты(опубликованные)из базы данных"""
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=dt.now(),
    ).select_related('category', 'location', 'author')


def index(request):
    """Представление главной страницы"""
    post_list = posts()[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    """Отоброжение всех делатей выбранной записи"""
    post = get_object_or_404(posts(), pk=id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Представление публикация в категории"""
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    post_list = posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
