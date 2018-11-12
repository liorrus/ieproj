from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('products', views.ProductView.as_view(), name='products'),
    path('<slug:slug>/products/', views.ProductOneView.as_view(), name='product'),
    path('<slug:slug>/parts/', views.PartOneView.as_view(), name='part'),
    path('parts', views.PartView.as_view(), name='parts'),
    path('<slug:slug>/suppliers/', views.SupplierOneView.as_view(), name='supplier'),
    path('suppliers', views.SupplierView.as_view(), name='suppliers'),
]