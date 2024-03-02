from django.contrib import admin
from django.urls import path
from e_learning import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='index'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_course, name='add'),
    path('details/<str:name>', views.details, name='details'),
    path('edit/<str:name>', views.edit_course, name='edit'),
    path('delete/<str:name>', views.delete_course, name='delete'),
    path('progress/<str:user>', views.progress, name='progress'),
    path('complete/<str:course>', views.complete_course, name='complete'),
    path('delete_from_progress/<str:course>', views.delete_from_progress, name='delete_progress')
]
