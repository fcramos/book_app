from django.conf.urls import url, include
from rest_framework import routers
from library.views import AuthorViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
