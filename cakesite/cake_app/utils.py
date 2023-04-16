def create_data_list(query_set, size):
    general_data_list = []
    number = 1
    for i in query_set:
        local_data_list = []
        local_data_list.append(f'{number}. {i.model_product}')
        number += 1
        all_quantity = i.quantity * size
        local_data_list.append(round(all_quantity, 3))
        local_data_list.append(i.model_product.price)
        all_price = i.model_product.price * all_quantity
        local_data_list.append(round(all_price, 2))
        general_data_list.append(local_data_list)
    return general_data_list


side_bar_admin = [
    {'link_name': 'Все изделия', 'url_name': 'index'},
    {'link_name': 'Только торты', 'url_name': 'onlycakes', 'attrs': 1},
    {'link_name': 'Только пироженое', 'url_name': 'onlycakes', 'attrs': 2},
    {'link_name': 'Все продукты', 'url_name': 'all_products'},
    {'link_name': 'Добавить продукт', 'url_name': 'add_product'},
    {'link_name': 'Добавить торт', 'url_name': 'add_cake'},
    {'link_name': 'Добавить тех-карту', 'url_name': 'add_techcard'},
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
