from django.urls import path
from . import views


urlpatterns = [
    path('create-shop/', views.create_shop, name='create-shop'),
    path('update-shop/<int:s_id>', views.update_shop, name='update-shop'),
    path('delete-shop/<int:s_id>', views.delete_shop, name='delete-shop'),
]
