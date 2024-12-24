from django.urls import path
from .views import despesa_create, despesa_list, despesa_update, despesa_delete

urlpatterns = [
    path('', despesa_list, name='despesa-list'),
    path('create/', despesa_create, name='despesa-create'),
    path('update/<int:pk>/', despesa_update, name='despesa-update'),
    path('delete/<int:pk>/', despesa_delete, name='despesa-delete'),
]