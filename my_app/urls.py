from django.urls import path
from my_app import views

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="get-products"),
    path("products/create/", views.ProductCreateView.as_view(), name="create-product"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name="get-product"),
    path("products/<int:pk>/update/", views.ProductUpdateView.as_view(), name="update-product"),
    path("products/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="delete-product"),
]