from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_view, name='registration'),
    path('success/', views.success_view, name='success'),
    path('registrations/', views.admin_registrations, name='admin_registrations'),
    path('admin_list/', views.admin_registrations, name='admin_list'),  # alias
]
