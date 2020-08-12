from django.contrib import admin
from django.urls import path
import mini_project.views as views
import exp.views as views2
import fas.views as views3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('food/', views.food),
    path('stay/', views.stay),
    path('festival/', views.festival),
    path('exp/', views.exp),
    path('expmap_data/', views2.expmap_data),
    path('fes_map/', views3.map_data),
]