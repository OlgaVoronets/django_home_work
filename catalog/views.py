from catalog.models import Product
from django.shortcuts import render, get_object_or_404


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': "Каталог продуктов"
    }
    return render(request, 'catalog/home.html', context)
    # return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя клиента: {name}\nКонтактный телефон: {phone}\nСообщение: {message}')
        # with open('info.txt', 'a', encoding='utf8') as file:
        #     file.write(f'Имя клиента: {name}\nКонтактный телефон: {phone}\nСообщение: {message}\n')
    return render(request, 'catalog/contacts.html')


def item(request, pk):

    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product,
        'title': "Карточка продукта",

    }
    return render(request, 'catalog/item.html', context)
