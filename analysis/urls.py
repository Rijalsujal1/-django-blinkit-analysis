from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('kpis/', views.KPIsView.as_view(), name='kpis'),
    path('sales-by-fat-content/', views.SalesByFatContentView.as_view(), name='sales_by_fat_content'),
    path('sales-by-item-type/', views.SalesByItemTypeView.as_view(), name='sales_by_item_type'),
    path('fat-content-by-outlet-sales/', views.FatContentByOutletSalesView.as_view(), name='fat_content_by_outlet_sales'),
    path('sales-by-outlet-establishment-year/', views.SalesByOutletEstablishmentYearView.as_view(), name='sales_by_outlet_establishment_year'),
    path('sales-by-outlet-size/', views.SalesByOutletSizeView.as_view(), name='sales_by_outlet_size'),
    path('sales-by-outlet-location/', views.SalesByOutletLocationView.as_view(), name='sales_by_outlet_location'),
    path('', views.index, name='index'),
]