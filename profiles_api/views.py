# from django.shortcuts import render
# we used views.py to link the templates
"""for api view:::"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers
from profiles_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated 


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions( get post put delete patch)',
            'Is similar to traditional django views',
            'Gives you most control over our app',
            'Is mapped manually to Urls',


        ]

        return Response({'message': 'hello',  'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""

        return Response({'method': 'PATCH'})

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test api ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello msg"""
        a_viewset = [
            'Users actions (list, create , update , partially update , destroy)',
            'automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({
            'message': f'Hello', 'a_viewset': a_viewset
        })

        # add a router for viewset to work

    def create(self, request):
        """Create a new hello msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle update object """

        return Response({'http_method': 'GET'})

    def partial_update(self, request, pk=None):
        """Handle updating a part of an object"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing the  object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication ,)
    permission_classes = (permissions.UpdateOwnProfile , )
    filter_backends =  (filters.SearchFilter,)
    search_fields = ('name', 'email')



class UserLoginApiView(ObtainAuthToken): 
    """Handle creating user authentication tokens"""

    renderer_classes  =  api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating , reading and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus , 
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Set the user profile to the logged in user"""

        serializer.save(user_profile = self.request.user)

