from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DetailView, UpdateView
from cake_app.utils import *
from .forms import *
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


class CakeDetailsView(DataMixin, DetailView):
    model = Cake
    template_name = 'cake_app/one_cake.html'
    diameter = {14: 0.765, 16: 1, 18: 1.2656, 20: 1.56}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cake = Cake.objects.get(slug=self.kwargs['slug'])
        try:
            techcard_list = get_techcard_list(cake.techcard, self.diameter[self.kwargs['size']])
        except:
            context_mixin = self.get_user_data(size=self.kwargs['size'],
                                               diameter=self.diameter,
                                               title=Cake.objects.get(
                                                   slug=cake.slug),
                                               techcard_list=None)
            return dict(list(context.items()) + list(context_mixin.items()))
        context_mixin = self.get_user_data(size=self.kwargs['size'],
                                           diameter=self.diameter,
                                           title=Cake.objects.get(
                                               slug=cake.slug),
                                           techcard_list=techcard_list)
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
                                           bar_selected='Все продукты',
                                           link_name='all_products'
                                           )
        return dict(list(context.items()) + list(context_mixin.items()))

    def post(self, request):
        if self.request.user.username == 'admin':
            data = list(request.POST.items())[1]
            product = Product.objects.get(name=data[0])
            if data[1]:
                product.price = round(float(data[1]), 2)
                product.save()
            else:
                product.delete()
            return redirect('all_products')
        return HttpResponseNotFound('Только администратор может изменять или удалять продукты.')


class AddProductView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'cake_app/add_element.html'
    success_url = reverse_lazy('all_products')
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
        return redirect('all_products')


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
        products = Product.objects.all()
        query_products = {'products': products}
        return dict(list(context.items()) + list(context_mixin.items()) + list(query_products.items()))

    def form_valid(self, form):
        dict_form = dict(form.data)
        try:
            json = create_json(dict_form['product'], dict_form['quantity'])
        except:
            form.add_error('type', 'Количество не может быть равно или меньше 0')
        if form.is_valid():
            if self.request.user.username == 'admin':
                form.save(json)
                return redirect('index')
            else:
                return HttpResponseNotFound('Только администратор может добавлять данные')
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(self.request, 'cake_app/add_element.html', context)


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


class CakeUpdateView(DataMixin, UpdateView):
    model = Cake
    form_class = CakeUpdateForm
    template_name = 'cake_app/change_techcard.html'
    context_object_name = 'cake'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_data(title='Изменить техкарту',
                                           link_name='change_techcard')
        techcard = context['cake'].techcard[0]
        techcard_context = {'techcard': list(techcard.values())}
        products = Product.objects.all()
        query_products = {'products': products}
        return dict(list(context.items()) + list(context_mixin.items()) + list(techcard_context.items()) + list(
            query_products.items()))

    def form_valid(self, form):
        dict_form = dict(form.data)
        try:
            json = create_json(dict_form['product'], dict_form['quantity'])
        except:
            form.add_error('type', 'Количество не может быть равно 0 или меньше')
        if form.is_valid():
            if self.request.user.username == 'admin':
                form.save(json)
                cake = Cake.objects.get(name=form.data['name'])
                return redirect(cake)
            else:
                return HttpResponseNotFound('Только администратор может вносить изменения')
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(self.request, 'cake_app/change_techcard.html', context)


def delete_cake(request, slug):
    if request.user.username == 'admin':
        cake = Cake.objects.get(slug=slug)
        cake.delete()
        return redirect('index')
    else:
        return HttpResponseNotFound('Только администратор может удалять данные')