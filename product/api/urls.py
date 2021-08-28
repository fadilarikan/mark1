from django.urls import path, include

from product.api.views import ProductListAPIView

urlpatterns = [
    path('list', ProductListAPIView.as_view(),name='list'),

]