from django.contrib import admin
from .models import Article

def make_published(self, request, queryset):
    queryset.update(status='p')   #sql 문 

make_published.short_description = "선택된 articles를 Published 상태로 변경합니다."

def make_draft(self, request, queryset):
    queryset.update(status='d')   #sql 문 

make_draft.short_description = "선택된 articles를 Drafted 상태로 변경합니다."


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published,make_draft]

admin.site.register(Article, ArticleAdmin)
