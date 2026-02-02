from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store_View, name='store'),
    path('product/<slug:slug>/', views.product_info, name='product-info')
]
