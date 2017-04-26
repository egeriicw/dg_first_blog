from django.conf.urls import url
from .views import AddressViewSet, PlaceViewSet
from rest_framework import routers


address_list = AddressViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

address_detail = AddressViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

place_list = PlaceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

place_detail = PlaceViewSet.as_view({
    'get': 'retrive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'place', PlaceViewSet)

urlpatterns = router.urls
