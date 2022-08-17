from django.contrib import admin
from .models import Article

def make_published(self, request, queryset):
    queryset.update(status='p')
    make_published.short_description = "선택된 articles를 Published 상태로 변경합니다."

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']

admin.site.register(Article, ArticleAdmin)
