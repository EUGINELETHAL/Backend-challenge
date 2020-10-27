from django.urls import path
from .import views 
from .views import OrderListCreateAPIView


app_name = 'core'
urlpatterns = [
    path('order', OrderListCreateAPIView.as_view(), name="list"),
    path('username',  views.print_username, name="username")
   
]

