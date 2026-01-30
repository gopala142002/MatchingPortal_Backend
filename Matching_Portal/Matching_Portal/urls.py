from django.contrib import admin
from django.urls import path, include  
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/auth/token/refresh/", TokenRefreshView.as_view()),
    path("api/files/", include("files.urls")),
    path("api/papers/", include("papers.urls")),
]