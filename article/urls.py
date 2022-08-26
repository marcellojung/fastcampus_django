from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.article_list,name='list'),
    path('<id>/detail/', views.detail,name='detail'),
    # path('new/', views.article_new, name='new'),
    # path('<pk>/edit/', views.article_edit, name='edit'),
    # path('<pk>/delete/', views.article_delete, name='delete'),
]
