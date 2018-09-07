from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('api/product_list/', views.ProductListCreate.as_view()),
    path('api/users/', views.UserViewSet.as_view()),
=======
    path('api/product_list/', views.ProductListCreate.as_view() ),

>>>>>>> 676bccfad4b5683ac66a1afab8b80958691e6bbd
]
