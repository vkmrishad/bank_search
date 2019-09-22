from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views as bank_view


router = DefaultRouter()
router.register(r'bank', bank_view.BankViewSet, 'bank')
router.register(r'branch', bank_view.BranchViewSet, 'branch')

urlpatterns = [
    path('', include(router.urls)),
]
