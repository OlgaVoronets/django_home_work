from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import ProductListView, contacts, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/view_product/', ProductDetailView.as_view(), name='view_product'),
    # path('<int:pk>/product/', product, name='product'),
]
