from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:visit_id>/', views.delete_visit, name='delete_visit'),
]
