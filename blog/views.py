from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from blog.forms import CommentForm

import logging # Used for logging
# Create your views here.

# logger
logger = logging.getLogger(__name__)

# return blog/index.html if request
def index(request):
    # return all posts
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug("Got %d posts", len(posts)) # logger
    return render(request, "blog/index.html", {"posts": posts})

# create post
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # fetching post
    if request.user.is_active: #  check if user logged in or not
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                # log if comment is Created
                logger.info("Created comment on Post %d for user %s", post.pk, request.user)
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None
    return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})