from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import Researcher

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    name = serializers.CharField()
    institution = serializers.CharField()
    department = serializers.CharField()
    academic_position = serializers.CharField()
    research_interests = serializers.ListField(
        child=serializers.CharField()
    )

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username=email,      
            email=email,
            password=password
        )

        Researcher.objects.create(
            user=user,
            name=validated_data["name"],
            institution=validated_data["institution"],
            department=validated_data["department"],
            academic_position=validated_data["academic_position"],
            research_interests=validated_data["research_interests"],
        )

        return user
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data["email"]
        password = data["password"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        user = authenticate(username=user.username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user
        return data
    
class ResearcherSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Researcher
        fields = [
            "id",
            "name",
            "email",
            "institution",
            "department",
            "academic_position",
            "research_interests",
            "h_index",
            "created_at",
        ]
