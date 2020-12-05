"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from products import views

app_name = 'products'
urlpatterns = [
    path('dont_do_this/', views.bad_view),
    path('search/', views.search_view),
    # re_path(r'products/(?P<id>\d+)/', views.product_api_detail_view),
    path('products/', views.product_list_view, name='product_list'), 
    path('products/create/', views.product_create_view), 
    
    path('products/<int:pk>/', views.product_api_detail_view),

    # path('products/1/', views.product_api_detail_view)    
]
