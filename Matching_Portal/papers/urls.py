from django.urls import path
from .views import PaperCreateView, PaperListView


urlpatterns = [
    path("create/", PaperCreateView.as_view()),
    path("", PaperListView.as_view()),
]
