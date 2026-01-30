from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import (
    RegisterSerializer,
    LoginSerializer,
    ResearcherSerializer,
)

from accounts.models import Researcher

@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        {"detail": "User registered successfully"},
        status=status.HTTP_201_CREATED
    )

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def verify_token(request):
    return Response({
        "status": True,
        "message": "Token is valid",
        "user": request.user.email
    })


@api_view(["POST"])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    isTokenValid = serializer.is_valid(raise_exception=False)

    if not isTokenValid :
        return Response({
            "status": False,
            "error": "Invalid" 
        })

    user = serializer.validated_data["user"]
    refresh = RefreshToken.for_user(user)

    return Response({
        "status": True,
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    })

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    researcher = request.user.researcher
    return Response(ResearcherSerializer(researcher).data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    refresh_token = request.data.get("refresh")
    if not refresh_token:
        return Response({"detail": "Refresh token required"}, status=400)
    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response({"detail": "Logged out successfully"})
