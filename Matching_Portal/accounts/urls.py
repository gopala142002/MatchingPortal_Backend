from django.urls import path
from accounts.views import (
    register,
    profile,
    logout_view,login_view
)

urlpatterns = [
    path("register/", register),
    path("login/", login_view),
    path("me/", profile),
    path("logout/", logout_view),
]
