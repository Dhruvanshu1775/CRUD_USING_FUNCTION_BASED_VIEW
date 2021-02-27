from django.urls import path, re_path
from . import views

urlpatterns= [
    path('',views.add_order,name='index'),
    path('detail/',views.orderdetail,name='detail'),
    path('update/<int:id><str:customer_name>',views.update),
    path('delete/<int:id><str:customer_name>',views.delete),
    path('get/',views.get.as_view()),
    path('post/',views.post.as_view()),
   
]