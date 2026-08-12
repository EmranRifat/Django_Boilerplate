from django.urls import path
from users import views


urlpatterns = [
    # Authentication
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),

    # User
    path("get-userlist/", views.UserListView.as_view(), name="user-list"),
    path("get-user/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),

    # Password
    path("forget-password/", views.ForgotPasswordView.as_view(), name="forget-password"),
    path("reset-password/", views.ResetPasswordView.as_view(), name="reset-password"),
]