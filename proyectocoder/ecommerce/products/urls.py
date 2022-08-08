from django.urls import path
from products.views import create_products, listar_productos

urlpatterns = [
    path('listar_productos/',listar_productos,name="listarproductos"),
    path('crear_producto/',create_products,name="createproducts"),
]
