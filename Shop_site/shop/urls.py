from django.urls import path
from shop.views import *
urlpatterns = [
    path('',index,name = 'index'),
    path("catalog/<str:slug>",Product_list.as_view(),name = 'Product_list'),
    path('product/<str:slug>',Single.as_view(),name = 'Single'),
    path('Hozproduct_catalog/<str:slug>',HozProduct_list.as_view(),name = 'HozProduct_list'),
    path('Hozproduct_product/<str:slug>',HozProduct_Single.as_view(),name = 'HozProduct_Single'),
    path('register/', register, name='register'),
    path('login/', loginuser, name='login'),
    path('cart/',cart,name='cart'),
    path('logout/',user_logout,name='logout'),
    path('orders/', Orders.as_view(), name = 'orders'),
    path('search/', Search.as_view(),name = 'search'),
    path('product_discont/',Discount_list.as_view(),name='discount_list'),
    path('hozproduct_discont/',Discount_list.as_view(),name='discount_hozlist'),
]