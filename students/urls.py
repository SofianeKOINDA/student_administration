from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('view/<int:student_id>/', views.view_student, name='view_student'),
]