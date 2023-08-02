from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import RegisterUserForm, LoginUserForm
from main.models import Items, Basket

@login_required
def basket(req):
    user = req.user
    items_id = []
    total_price = []
    basket = {}
    item_id = Basket.objects.filter(user=user)
    for id in item_id:
        items_id.append(int(id.id_tovara))
        basket[id.id_tovara] = int(id.amount_of_items)
    items = Items.objects.filter(pk__in=items_id)
    for item in items:
        total_price.append(int(item.price.replace(' ', '')) * int(basket[str(item.pk)]))
    context = {
        'items': items,
        'total_price': sum(total_price),
        'basket': basket,
    }
    return render(req, 'main/basket.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(req):
    logout(req)
    return redirect('login')

