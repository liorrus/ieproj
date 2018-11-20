from django.urls import path
from django.urls import include,re_path
from . import views
from .views import LoginView, OrderUser
from django.views.generic.base import RedirectView


app_name = 'polls'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
    re_path(r'^order/$', views.OrderUser.as_view(), name='order'),
    #re_path(r'^(?P<pk>[0-9a-z-]+)/$', views.OrderUser.as_view(), name='order'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('products', views.ProductView.as_view(), name='products'),
    path('<slug:slug>/products/', views.ProductOneView.as_view(), name='product'),
    path('extras', views.ExtraView.as_view(), name='extras'),
    path('<slug:slug>/extras/', views.ExtraOneView.as_view(), name='extra'),
    path('<slug:slug>/parts/', views.PartOneView.as_view(), name='part'),
    path('parts', views.PartView.as_view(), name='parts'),
    path('<slug:slug>/suppliers/', views.SupplierOneView.as_view(), name='supplier'),
    path('suppliers', views.SupplierView.as_view(), name='suppliers'),
    path('orders', views.OrderView.as_view(), name='orders'),
    path('create/order', views.OrderCreate.as_view(), name='order_create'),
]
