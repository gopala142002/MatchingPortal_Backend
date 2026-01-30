from rest_framework import generics, permissions
from .models import Paper
from .serializers import PaperSerializer


class PaperCreateView(generics.CreateAPIView):
    serializer_class = PaperSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PaperListView(generics.ListAPIView):
    serializer_class = PaperSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Paper.objects.filter(author=self.request.user)
