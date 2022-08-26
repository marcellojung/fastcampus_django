from django.contrib import admin
from .models import Post,Comment,Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','updated_at']
    def content_size(self,post):
        return f'{len(post.content)}글자'
    content_size.short_description='글자수'
    list_display_links = ['id','title']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)


