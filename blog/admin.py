from django.contrib import admin
from .models import Post,Comment,Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at']
    list_display_links = ['id','title']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)


