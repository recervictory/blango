from django.shortcuts import render
# Developer Import
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404

# comment forms
from django.shortcuts import redirect
from blog.forms import CommentForm
# logging
import logging
logger = logging.getLogger(__name__) # name is the module name
# Cache page
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

@cache_page(300)
@vary_on_headers('cookie')
def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  # Logging
  logger.debug("Got %d posts", len(posts))
  return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
      if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.content_object = post
          comment.creator = request.user
          comment.save()
          # Logging
          logger.info("Created comment on Post %d for user %s", post.pk, request.user)
          return redirect(request.path_info)
      else:
        comment_form = CommentForm()
    else:
        comment_form = None
    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )