from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group

POSTS_COUNT = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:POSTS_COUN]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_COUN]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
