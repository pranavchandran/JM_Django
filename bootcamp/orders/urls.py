
from django.contrib import admin
from django.urls import include, path
from orders import views
app_name = 'orders'

urlpatterns = [
    path('checkout/', views.order_checkout_view),
    
]