from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import AddItemForm
from .models import *
def home(req):
    items = Items.objects.all()
    categories = Categories.objects.all()
    user = req.user
    basket = Basket.objects.filter(user=user)
    amount_of_items = []
    bought_items = []
    basket_update = {}
    for item in basket:
        bought_items.append(int(item.id_tovara))
        basket_update[item.id_tovara] = int(item.amount_of_items)
        amount_of_items.append(1 * int(item.amount_of_items))
    if req.method == 'POST':
        form = AddItemForm(req.POST)
        if form.is_valid():
            try:
                Basket.objects.create(user=user, **form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddItemForm()
    context = {
        'items': items,
        'form': form,
        'categories': categories,
        'amount_of_items': sum(amount_of_items),
        'bought_items': bought_items,
        'basket': basket_update,
    }
    return render(req, 'main/home.html', context=context)

def show_category(request, cat_id):
    user = request.user
    items = Items.objects.filter(cat_id=cat_id)
    categories = Categories.objects.all()
    basket = Basket.objects.filter(user=user)
    amount_of_items = len(basket)
    context = {
        'items': items,
        'categories': categories,
        'title': 'Главная страница',
        'cat_selected': cat_id,
        'amount_of_items': amount_of_items,
    }

    return render(request, 'main/home.html', context=context)


def show_item(request, item_slug):
    item = get_object_or_404(Items, slug=item_slug)
    user = request.user
    basket = Basket.objects.filter(user=user)
    basket_update = {}
    bought_items = []
    for i in basket:
        bought_items.append(i.id_tovara)
        basket_update[i.id_tovara] = int(i.amount_of_items)
    bought_items = [int(i) for i in bought_items]
    context = {
        'item': item,
        'title': f'{item.title}',
        'bought_items': bought_items,
        'basket': basket_update,
    }

    return render(request, 'main/item.html', context=context)



def update_amount(request, item_id):
    item = get_object_or_404(Basket, id_tovara=item_id)

    if request.method == 'POST':
        form = AddItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('basket')

    # Если это GET-запрос, просто отобразите шаблон с формой обновления
    form = AddItemForm(instance=item)
    context = {'form': form, 'item': item}
    return render(request, 'main/basket.html', context)
