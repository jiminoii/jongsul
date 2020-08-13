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
    path('exp/', views.exp),
    path('expmap_data/', views2.expmap_data),
    path('foodmap_data/', views4.foodmap_data),
    path('fes_map/', views3.map_data),
    path('commu/write/', views.write),
    path('commu/list/', views.list),
    path('commu/success/', views.write),
    path('commu/fail/', views.write),
    path('user/list', views.list),
    path('commu/detail/<int:id>/', views.detail),



]
