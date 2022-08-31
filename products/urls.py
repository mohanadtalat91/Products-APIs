from django.urls import path
from . import views

urlpatterns = [
    path('AllProducts', views.All_Products),
    path('AddProduct', views.Add_Product),
    path('GetProduct/<int:id>', views.Get_Product),
    path('UpdateProduct/<int:id>', views.Update_Product),
    path('DeleteProduct/<int:id>', views.Delete_Product),
]