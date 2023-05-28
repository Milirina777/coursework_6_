from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

user_router = SimpleRouter()
user_router.register(prefix='', viewset=UserViewSet, basename='users')

urlpatterns = [
    path("", include(user_router.urls))
]
