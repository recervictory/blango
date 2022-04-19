from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.

# return blog/index.html if request
def index(request):
    # return all posts
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
