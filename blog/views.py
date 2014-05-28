from django.shortcuts import render

# Create your views here.
from blog.models import Post


def about(request):
    return render(request, "blog/about.html", {'nav_about': True, 'page_title': "Deadlock"})


def blog(request):
    posts = Post.objects.filter(publish=True).order_by("-pub_date")[:10]
    latest_post = None
    if len(posts):
        latest_post = posts[0]
    return render(request, "blog/blog.html", {'posts': posts,
                                               'latest_post': latest_post,
                                               'nav_blog': True,
                                               'page_title': "Deadlock - Blog"})


def post(request, slug):
    active_post = Post.objects.get(slug=slug)
    posts = Post.objects.filter(publish=True).order_by("-pub_date")[:10]
    latest_post = None
    if len(posts):
        latest_post = posts[0]
    return render(request, "blog/blog.html", {'posts': posts,
                                               'latest_post': latest_post,
                                               'active_post': active_post,
                                               'nav_blog': True,
                                               'page_title': "Deadlock - %s" % active_post.title})
