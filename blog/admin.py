from django.contrib import admin
from blog.models import Tag, Post, Comment

# Register your models here.



# Admin View Change
class PostAdmin(admin.ModelAdmin):
  prepopulated_feilds = {'slug': ('title', )}
  list_display = ('slug', 'published_at')


# Register Models
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
