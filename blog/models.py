from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
#from blog.models import Post
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone
# Create your models here.
class Tag(models.Model):
  # Tag contains tag text
  value = models.TextField(max_length = 100)

  def __str__(self):
    return self.value

# Comment Model implemented with GenericForeignKey
class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
  # The post by user
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
  created_at = models.DateTimeField(auto_now_add = True,db_index=True)
  modified_at = models.DateTimeField(auto_now = True)
  published_at = models.DateTimeField(blank = True, null = True)
  title = models.TextField(max_length = 100)
  slug = models.SlugField(unique=True)
  summary = models.TextField(max_length = 500)
  content = models.TextField()
  tags = models.ManyToManyField(Tag, related_name = "posts")
  comments = GenericRelation(Comment)

  def __str__(self):
    return self.title

'''
# Comment Model implemented with ForeignKey
class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
'''

# SQL Optimization
published_at = models.DateTimeField(blank=True, null=True, db_index=True)
posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
'''
posts = (
    Post.objects.filter(published_at__lte=timezone.now())
    .select_related("author")
    .only("title", "summary", "content", "author", "published_at", "slug")
)
'''