from django.contrib import admin
from django.urls import path
import mini_project.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('food/', views.food),
    path('stay/', views.stay),
    path('festival/', views.festival),
    path('exp/', views.exp),
<<<<<<< HEAD
]
=======
]
>>>>>>> fb4cfae32d8c88a2ef593e18bd849bdf6f41eb53
