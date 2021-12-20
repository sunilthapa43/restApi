from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('hello-viewset', views.HelloViewSet ,basename ='hello-viewset')
router.register('profile', views.UserProfileViewSet , basename = 'profile')
router.register('feed', views.UserProfileViewSet , basename = 'feed')


urlpatterns=[
  path('hello_view/', views.HelloApiView.as_view(), name='hello'),
  path('login/', views.UserLoginApiView.as_view()),
  path('',include(router.urls)),

]