from django.urls import path
from . import views

urlpatterns= [
    path('',views.add_order,name='index'),
    path('detail/',views.orderdetail,name='detail'),
   
]