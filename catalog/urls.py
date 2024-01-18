from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, published_toggle

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/view_product/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('<int:pk>/edit_product/', ProductUpdateView.as_view(), name='edit_product'),
    path('<int:pk>/product/', ProductDeleteView.as_view(), name='delete_product'),
    path('<int:pk>/published/', published_toggle, name='published_toggle')
]
