from django.contrib import admin
from django.urls import path
import mini_project.views as views
import exp.views as views2
import food.views as views4
import fas.views as views3



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('food/', views.food),
    path('stay/', views.stay),
    path('festival/', views.festival),
    path('festival2/', views.festival2),
    path('festival3/', views.festival3),
    path('festival4/', views.festival4),
    path('exp/', views.exp),
    path('expmap_data/', views2.expmap_data),
    path('foodmap_data/', views4.foodmap_data),
    path('fes_map/', views3.map_data),
    path('commu_write/', views.write),
    path('user/list/', views.write),


]
