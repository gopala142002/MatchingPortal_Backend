from rest_framework import serializers
from .models import Paper


class PaperSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Paper
        fields = "__all__"
