from django.urls import path
from django.urls import include,re_path
from django.conf.urls import url
from . import views
from .views import LoginView
from django.views.generic import CreateView
from django.views.generic.base import RedirectView


app_name = 'polls'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
    path('orders', views.OrderView.as_view(), name='orders'),
    path('create/order', views.OrderCreateAdmin.as_view(), name='order_create'),
    re_path(r'order_costumer/$', views.OrderCreateCustomer.as_view(), name="order_costumer"),
    path('order_ok', views.OrderDetailView.as_view(), name='order_ok'),
    url(r'add_product/$', views.ProductCreate.as_view(), name="product-add"),
    url(r'add_part/$', views.PartCreate.as_view(), name="part-add"),
    url(r'add_supplier/$', views.SupplierCreate.as_view(), name="supplier-add"),
    url(r'add_partsinproduct/$', views.PartsInProductCreate.as_view(), name="partsinproduct-add"),
    url(r'add_order/$', views.OrderCreateAdmin.as_view(), name="order-add"),
    url(r'^product(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    re_path(r'^adminsite/$', views.AdminView.as_view(), name='adminsite'),
    url(r'product_index/$', views.ProductIndexView.as_view(), name="product_index"),
    url(r'^order(?P<pk>[0-9]+)/$', views.OrderDetailView.as_view(), name='order_detail'),
    url(r'order_index/$', views.OrderIndexView.as_view(), name="order_index"),

]
