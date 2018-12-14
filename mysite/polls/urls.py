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
    url(r'add_pip/$', views.PipCreate.as_view(), name="pip-add"),
    url(r'add_order/$', views.OrderCreateAdmin.as_view(), name="order-add"),
    url(r'add_components/$', views.ComponentsCreate.as_view(), name="components-add"),
    url(r'add_extras/$', views.ExtrasCreate.as_view(), name="newextra-add"),
    url(r'add_supprice/$', views.SuppriceCreate.as_view(), name="supprice-add"),
    url(r'add_pord/$', views.PordCreate.as_view(), name="pord-add"),
    url(r'add_porderitem/$', views.PorderitemCreate.as_view(), name="porderitem-add"),
    re_path(r'^adminsite/$', views.AdminView.as_view(), name='adminsite'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^product_index/$', views.ProductIndexView.as_view(), name="product_index"),
    url(r'product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name="product_update"),
    url(r'product/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name="product_delete"),
    url(r'^order(?P<pk>[0-9]+)/$', views.OrderDetailView.as_view(), name='order_detail'),
    url(r'order_index/$', views.OrderIndexView.as_view(), name="order_index"),
    url(r'^part(?P<pk>[0-9]+)/$', views.PartDetailView.as_view(), name='part_detail'),
    url(r'part_index/$', views.PartIndexView.as_view(), name="part_index"),
    url(r'^pip(?P<pk>[0-9]+)/$', views.PipDetailView.as_view(), name='pip_detail'),
    url(r'pip_index/$', views.PipIndexView.as_view(), name="pip_index"),
    url(r'^supplier(?P<pk>[0-9]+)/$', views.SupplierDetailView.as_view(), name='supplier_detail'),
    url(r'supplier_index/$', views.SupplierIndexView.as_view(), name="supplier_index"),
    url(r'^components(?P<pk>[0-9]+)/$', views.ComponentsDetailView.as_view(), name='components_detail'),
    url(r'components_index/$', views.ComponentsIndexView.as_view(), name="components_index"),
    url(r'^extras(?P<pk>[0-9]+)/$', views.ExtrasDetailView.as_view(), name='newextra_detail'),
    url(r'extras_index/$', views.ExtrasIndexView.as_view(), name="newextra_index"),
    url(r'^supprice(?P<pk>[0-9]+)/$', views.SuppriceDetailView.as_view(), name='supprice_detail'),
    url(r'supprice_index/$', views.SuppriceIndexView.as_view(), name="supprice_index"),
    url(r'^pord(?P<pk>[0-9]+)/$', views.PordDetailView.as_view(), name='pord_detail'),
    url(r'pord_index/$', views.PordIndexView.as_view(), name="pord_index"),
    url(r'^porderitem(?P<pk>[0-9]+)/$', views.PorderitemDetailView.as_view(), name='porderitem_detail'),
    url(r'porderitem_index/$', views.PorderitemIndexView.as_view(), name="porderitem_index"),







]
