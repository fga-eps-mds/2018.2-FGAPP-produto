from django.urls import path
from . import views

urlpatterns = [
    path('api/product_list/', views.ProductListCreate.as_view() ),

]