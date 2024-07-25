from django.urls import path
from . import views

urlpatterns = [
    path('menu/<str:menu_name>/', views.menu, name='menu'),

]