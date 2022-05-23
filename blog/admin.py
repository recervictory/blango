from django.contrib import admin
from blog.models import Tag, Post

# Register your models here.

# Register Tag
admin.site.register(Tag)

# Register Post
class PostAdmin(admin.ModelAdmin):
  prepopulated_feilds = {'slug': ('title', )}
  list_display = ('slug', 'published_at')

admin.site.register(Post, PostAdmin)
