from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('register/', views.register,name='register'),
    path('branch/', views.branch, name='branch'),
    path('thrissur/', views.thrissur, name='thrissur'),
    path('ernakulam/', views.ernakulam, name='ernakulam'),
    path('calicut/', views.calicut, name='calicut'),
    path('trivandrum/', views.trivandrum, name='trivandrum'),
    path('palghat/', views.palghat, name='palghat'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX

]