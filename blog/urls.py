from django.urls import path

from blog.apps import BlogConfig

app_name = BlogConfig

urlpatterns = [
    # path('', ProductListView.as_view(), name='home'),
    # path('contacts/', contacts, name='contacts'),
    # path('<int:pk>/view_product/', ProductDetailView.as_view(), name='view_product'),
    # path('<int:pk>/product/', product, name='product'),
]