from django.urls import path
from  course import views

urlpatterns= [
    path('',views.home,name = 'home'),
    path('course/views',views.data_render,name='data_render'),

]