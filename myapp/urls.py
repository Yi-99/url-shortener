from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from myapp.views import UrlViewSet

router = DefaultRouter()
router.register(r'urls', UrlViewSet)

urlpatterns = [
    path('', views.shorten_url, name='shorten'),
    path('<str:short_url>', views.redirect_to_original, name='redirect'),
]