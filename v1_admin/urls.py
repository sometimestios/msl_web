from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log_check/', views.log_check, name='log_check'),
    path('log_add/', views.log_add, name='log_add'),
    path('target_check/', views.tartget_check, name='target_check'),
    path('target_add/', views.target_add, name='target_add'),
    path('target_form/', views.target_form, name='target_form'),
    path('task_manage/', views.task_manage, name='task_manage'),
]
