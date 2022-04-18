from blog.models import Tag, Post
from django.contrib import admin

# Register your models here.
admin.site.register(Tag)

# slugfy
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

