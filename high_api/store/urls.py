from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import OrderViewSet, OrderItemViewSet, PaymentViewSet, ReviewViewSet, CategoryViewSet, ProductViewSet
from .views import RegistrationAPIView, LoginAPIView

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'orderitems', OrderItemViewSet, basename='orderitem')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('register/', RegistrationAPIView.as_view(), name='user-registration'),
]