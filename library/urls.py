from django.conf.urls import url, include
from rest_framework import routers
from library.views import AuthorViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
