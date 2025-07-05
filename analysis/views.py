from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from .utils import (
    load_and_preprocess_data,
    get_kpis,
    plot_sales_by_fat_content,
    plot_sales_by_item_type,
    plot_fat_content_by_outlet_sales,
    plot_sales_by_outlet_establishment_year,
    plot_sales_by_outlet_size,
    plot_sales_by_outlet_location
)

DATA_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'blinkit_data.csv')

# Load and preprocess data once
df = load_and_preprocess_data(DATA_FILE_PATH)

def hello_world(request):
    return HttpResponse("Hello, world! This is the analysis app.")

class KPIsView(APIView):
    def get(self, request):
        kpis = get_kpis(df)
        return Response(kpis)

class SalesByFatContentView(APIView):
    def get(self, request):
        graphic = plot_sales_by_fat_content(df)
        return Response({'image': graphic})

class SalesByItemTypeView(APIView):
    def get(self, request):
        graphic = plot_sales_by_item_type(df)
        return Response({'image': graphic})

class FatContentByOutletSalesView(APIView):
    def get(self, request):
        graphic = plot_fat_content_by_outlet_sales(df)
        return Response({'image': graphic})

class SalesByOutletEstablishmentYearView(APIView):
    def get(self, request):
        graphic = plot_sales_by_outlet_establishment_year(df)
        return Response({'image': graphic})

class SalesByOutletSizeView(APIView):
    def get(self, request):
        graphic = plot_sales_by_outlet_size(df)
        return Response({'image': graphic})

class SalesByOutletLocationView(APIView):
    def get(self, request):
        graphic = plot_sales_by_outlet_location(df)
        return Response({'image': graphic})


def index(request):
    context = {
        'kpis': get_kpis(df),
        'sales_by_fat_content_chart': plot_sales_by_fat_content(df),
        'sales_by_item_type_chart': plot_sales_by_item_type(df),
        'fat_content_by_outlet_sales_chart': plot_fat_content_by_outlet_sales(df),
        'sales_by_outlet_establishment_year_chart': plot_sales_by_outlet_establishment_year(df),
        'sales_by_outlet_size_chart': plot_sales_by_outlet_size(df),
        'sales_by_outlet_location_chart': plot_sales_by_outlet_location(df),
    }
    return render(request, 'analysis/index.html', context)
