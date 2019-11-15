from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
router = DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='posts')


urlpatterns = [
    path('', include(router.urls)),
]
