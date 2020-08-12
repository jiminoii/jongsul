from django.contrib import admin
from django.urls import path
import mini_project.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('food/<int:id>', views.food),
    path('stay/', views.stay),
    path('festival/', views.festival),
    path('exp/', views.exp),
]