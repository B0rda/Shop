from django.urls import path
from .views import *


urlpatterns = [
    path('all_product/', ApiAllProduct.as_view()),
    path('all_hozproduct/', ApiAllHozproduct.as_view()),
    path('detail_product/<int:pk>',ApiDetailProduct.as_view()),
    path('detail_hozproduct/<int:pk>',ApiDetailHozProduct.as_view()),
]