"""Users views."""

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
#from cride.users.permissions import IsAccountOwner

# Serializers 
from users.serializers.users import UserSignUpModelSerializer, UserModelSerializer, UserLoginSerializer

# Models
from users.models.users import User

class UserViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """
    queryset = User.objects.filter(is_active=True)
    #serializer_class = UserModelSerializer
    lookup_field = 'username'
    
    # solo accesible por usuario    
    """
    def get_permissions(self):
        if self.action in ['signup', 'login']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permissions = [IsAuthenticated, ] #IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]
    """
    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'signup':
            return UserSignUpModelSerializer
        return UserModelSerializer


    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User log in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        
        response = Response(data, status=status.HTTP_200_OK)
        response.set_cookie(key='access_token', value=token, httponly=True, samesite='None')
        print(data)
        return response

    @action(detail=False, methods=['get'])
    def logout(self, request):
        """User log out."""
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie(key='access_token')
        print("sesion cerrada")
        return response

    
    

    
    
    """
    @action(detail=False, methods=['post'])
    def verify(self, request):
        Account verification.
        # Handle HTTP POST request.
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulations, now go some rides!'}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods = ['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        Update profile data.
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        Add extra data to the response.
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        circles = Circle.objects.filter(
            members = request.user,
            membership__is_active=True
        )
        data = {
            'user': response.data,
            'circles': CircleModelSerializer(circles, many=True).data
        }
        response.data = data
        return response
        """