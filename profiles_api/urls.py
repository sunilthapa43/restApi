from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('hello-viewset', views.HelloViewSet ,'hello-viewset')

urlpatterns=[
  path('hello_view/', views.HelloApiView.as_view(), name='hello'),
  path('',include(router.urls)),

]