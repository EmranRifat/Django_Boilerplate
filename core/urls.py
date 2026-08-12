from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/users/", include("users.urls")),
    # path("api/products/", include("products.urls")),
    # path("api/orders/", include("order.urls")),
    # path("api/payments/", include("payment.urls")),

    # my_app CRUD
    path("api/", include("my_app.urls")),
]