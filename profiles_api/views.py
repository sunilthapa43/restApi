# from django.shortcuts import render
# we used views.py to link the templates
"""for api view:::"""

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview=[
        'Uses HTTP methods as functions( get post put delete patch)',
        'Is similar to traditional django views',
        'Gives you most control over our app',
        'Is mapped manually to Urls',


        ]

        return Response({'message':'hello',  'an_apiview': an_apiview})
