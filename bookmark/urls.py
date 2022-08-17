from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmark_list),
    path('<pk>/', views.bookmark_detail),
]
