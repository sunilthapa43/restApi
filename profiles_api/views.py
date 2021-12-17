# from django.shortcuts import render
# we used views.py to link the templates
"""for api view:::"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview=[
        'Uses HTTP methods as functions( get post put delete patch)',
        'Is similar to traditional django views',
        'Gives you most control over our app',
        'Is mapped manually to Urls',


        ]

        return Response({'message':'hello',  'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid() :
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


    def patch(self , request, pk = None):
        """Handle a partial update of an object"""

        return Response({'method': 'PATCH'})


    def put(self, request, pk= None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})



    def delete(self, request , pk = None):
        """Delete an object"""
        return Response({'method': 'DELETE'})





class HelloViewSet(viewsets.ViewSet):
    """Test api ViewSet"""
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
