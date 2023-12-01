from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('edit/<entry_id>', views.edit, name='edit'),
    path('delete/<entry_id>', views.delete, name='delete'),

]