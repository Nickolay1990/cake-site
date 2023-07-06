from cake_app.models import Product


def get_techcard_list(json_string, size):
    final_data = []
    for value in json_string[0].values():
        name = value['name']
        quantity = round(float(value['quantity']) * size, 2)
        price = Product.objects.get(name=name).price
        sum_of_price = round(quantity * price, 2)
        temp_data = [name, quantity, price, sum_of_price]
        final_data.append(temp_data)
    return final_data


side_bar_admin = [
    {'link_name': 'Все изделия', 'url_name': 'index'},
    {'link_name': 'Только торты', 'url_name': 'onlycakes', 'attrs': 1},
    {'link_name': 'Только пироженое', 'url_name': 'onlycakes', 'attrs': 2},
    {'link_name': 'Все продукты', 'url_name': 'all_products'},
    {'link_name': 'Добавить продукт', 'url_name': 'add_product'},
    {'link_name': 'Добавить торт', 'url_name': 'add_cake'},
]

side_bar_user = [
    {'link_name': 'Все изделия', 'url_name': 'index'},
    {'link_name': 'Только торты', 'url_name': 'onlycakes', 'attrs': 1},
    {'link_name': 'Только пироженое', 'url_name': 'onlycakes', 'attrs': 2},
    {'link_name': 'Все продукты', 'url_name': 'all_products'},
]

menu = [
    {'link_name': 'Контакты', 'url_name': 'contact'},
    {'link_name': 'О сайте', 'url_name': 'about'}
]


class DataMixin:
    def get_user_data(self, **kwargs):
        context_mixin = kwargs
        context_mixin['menu'] = menu
        if self.request.user.username == 'admin':
            context_mixin['side_bar'] = side_bar_admin
        else:
            context_mixin['side_bar'] = side_bar_user
        if 'menu_selected' not in context_mixin:
            context_mixin['menu_selected'] = 0
        return context_mixin


def create_json(products, quantity):
    final_dict = {}
    number = 1
    for key, value in zip(products, quantity):
        if float(value) <= 0:
            raise ValueError('Количество не может быть меньше 0*')
        new_dict = {f'product {number}': {'name': key, 'quantity': value}}
        number += 1
        final_dict.update(new_dict)
    return final_dict


def get_sum_of_quantity(techcard_list):
    sum_of_quantity = 0
    for element in techcard_list:
        sum_of_quantity += element[1]
    return round(sum_of_quantity, 2)
