from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product
from django.shortcuts import render, get_object_or_404



class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': "Каталог продуктов",
    }


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя клиента: {name}\nКонтактный телефон: {phone}\nСообщение: {message}')
        # with open('info.txt', 'a', encoding='utf8') as file:
        #     file.write(f'Имя клиента: {name}\nКонтактный телефон: {phone}\nСообщение: {message}\n')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': "Карточка продукта",
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
