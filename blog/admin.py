from blog.models import Tag, Post
from django.contrib import admin

# slugfy
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')


# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

