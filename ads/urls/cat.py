from django.urls import path
from rest_framework.routers import SimpleRouter

from ads.views.cat import *

router = SimpleRouter()
router.register("", CategoryViewSet)

urlpatterns = [
]

urlpatterns += router.urls
