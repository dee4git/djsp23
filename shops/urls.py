from django.urls import path
from . import views


urlpatterns = [
    path('create-shop/', views.create_shop, name='create-shop'),
    path('update-shop/<int:s_id>', views.update_shop, name='update-shop'),
    path('delete-shop/<int:s_id>', views.delete_shop, name='delete-shop'),
    path('view-products/<int:s_id>', views.view_products, name='view-products'),
    path('create-products/<int:s_id>', views.create_product, name='create-product'),
    path('update-products/<int:p_id>', views.update_product, name='update-product'),
]
