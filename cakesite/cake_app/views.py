from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from cake_app.utils import *
from .forms import *
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin


class CakeListView(DataMixin, ListView):
    paginate_by = 5
    model = Cake
    template_name = 'cake_app/index.html'
    context_object_name = 'cakes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(bar_selected='Все изделия',
                                           title='Все изделия')
        return dict(list(context.items()) + list(context_mixin.items()))


class OnlyCakeListView(DataMixin, ListView):
    paginate_by = 5
    model = Cake
    template_name = 'cake_app/index.html'
    context_object_name = 'cakes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['type'] == 1:
            context_mixin = self.get_user_data(bar_selected='Только торты',
                                           title='Торты')
        elif self.kwargs['type'] == 2:
            context_mixin = self.get_user_data(bar_selected='Только пироженое',
                                               title='Пироженое')
        else:
            context_mixin = {}
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_queryset(self):
        if self.kwargs['type'] == 1:
            queryset = Cake.objects.filter(type=1)
        elif self.kwargs['type'] == 2:
            queryset = Cake.objects.filter(type=2)
        else:
            queryset = []
        return queryset


class CakeDetailsView(DataMixin, ListView):
    model = TechCard
    template_name = 'cake_app/one_cake.html'
    context_object_name = 'records'
    diameter = {14: 0.765, 16: 1, 18: 1.2656, 20: 1.56}

    def get_queryset(self):
        query_set = TechCard.objects.filter(
            model_cake__slug=self.kwargs['slug'])
        records = create_data_list(query_set=query_set,
                                   size=self.diameter[self.kwargs['size']])
        return records

    def get_sum_of_quantity(self):
        quantity_sum = TechCard.objects.filter(
            model_cake__slug=self.kwargs['slug']).aggregate(
            sum=Sum('quantity'))
        return quantity_sum['sum']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_sum_of_quantity() != None:
            context_mixin = self.get_user_data(size=self.kwargs['size'],
                                               diameter=self.diameter,
                                               title=Cake.objects.get(
                                                   slug=self.kwargs['slug']),
                                               sum_of_quantity=round(
                                                   self.get_sum_of_quantity() *
                                                   self.diameter[
                                                       self.kwargs['size']],
                                                   2))
        else:
            context_mixin = self.get_user_data(
                title='Техкарты по данному торту отсутствуют')
        return dict(list(context.items()) + list(context_mixin.items()))


class ProductsListView(DataMixin, ListView):
    paginate_by = 100
    model = Product
    template_name = 'cake_app/all_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().order_by('name')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='Все продукты',
                                           bar_selected='Все продукты')
        return dict(list(context.items()) + list(context_mixin.items()))


class AddProductView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'cake_app/add_element.html'
    success_url = reverse_lazy('index')
    login_url = HttpResponseNotFound()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='Добавление продукта',
                                           link_name='add_product',
                                           bar_selected='Добавить продукт')
        return dict(list(context.items()) + list(context_mixin.items()))

    def form_valid(self, form):
        if self.request.user.username == 'admin':
            form.save()
        else:
            return HttpResponseNotFound('Only admin can to add post')
        return redirect('index')


class AddCakeView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCakeForm
    template_name = 'cake_app/add_element.html'
    success_url = reverse_lazy('index')
    login_url = HttpResponseNotFound()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='Добавление торта',
                                           link_name='add_cake',
                                           bar_selected='Добавить торт')
        return dict(list(context.items()) + list(context_mixin.items()))

    def form_valid(self, form):
        if self.request.user.username == 'admin':
            form.save()
        else:
            return HttpResponseNotFound('Only admin can to add post')
        return redirect('index')


class AddTechCardView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTechCardForm
    template_name = 'cake_app/add_element.html'
    success_url = reverse_lazy('add_techcard')
    login_url = HttpResponseNotFound()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='Добавление тех-карты',
                                           link_name='add_techcard',
                                           bar_selected='Добавить тех-карту')
        return dict(list(context.items()) + list(context_mixin.items()))

    def form_valid(self, form):
        if self.request.user.username == 'admin':
            form.save()
        else:
            return HttpResponseNotFound('Only admin can to add post')
        return redirect('add_techcard')


class RegisterView(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'cake_app/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='Регистрация',
                                           menu_selected='Регистрация')
        return dict(list(context.items()) + list(context_mixin.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUserView(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'cake_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='Войти',
                                           menu_selected='Войти')
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'cake_app/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='Контакты',
                                           menu_selected='Контакты')
        return dict(list(context.items()) + list(context_mixin.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('index')


class AboutView(DataMixin, ListView):
    model = Cake
    template_name = 'cake_app/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='О сайте',
                                           menu_selected='О сайте')
        return dict(list(context.items()) + list(context_mixin.items()))


def logout_user(request):
    logout(request)
    return redirect('index')

