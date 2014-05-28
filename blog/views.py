from django.shortcuts import render

# Create your views here.
from blog.models import Post


def index(request):
    posts = Post.objects.filter(publish=True).order_by("-pub_date")[:10]
    latest_post = None
    if len(posts):
        latest_post = posts[0]
    return render(request, "blog/index.html", {'posts': posts, 'latest_post': latest_post})


def post(request, slug):
    active_post = Post.objects.get(slug=slug)
    posts = Post.objects.filter(publish=True).order_by("-pub_date")[:10]
    latest_post = None
    if len(posts):
        latest_post = posts[0]
    return render(request, "blog/index.html", {'posts': posts, 'latest_post': latest_post, 'active_post': active_post})