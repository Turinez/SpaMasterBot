from collections import namedtuple


def sort_key(e):
    return e[3]


def to_string(product_list):
    return f"Косметика {str(product_list[1])} фирмы {str(product_list[0])} стоимостью {str(product_list[3])} рублей"


product = namedtuple('Product', ('manufacturer', 'series', 'purpose', 'price'))


def search(professional=None):
    # selected_products = ... products
    if professional is None:
        selected_products = products
    elif professional is True:
        selected_products = []
        for i in products:
            if i.series == 'профессиональная':
                selected_products.append(i)
        # бежим по списку продуктов и если в нем есть во втором
        # столбце записана профессиональная косметика, то мы заносим
        # все строчку в свой новый список

    sorted_products = sorted(selected_products, key=sort_key)
    to_print = sorted_products[0:10]
    return to_print



def get_prof_cos():

    indices = [element for element in products if element[1] == 'профессиональная']
    print(indices)
    return indices

def home():
    home_products = list(filter(lambda x: x[1] == 'домашняя', products))
    print(*home_products, sep="\n")


def proff():
    proff_products = list(filter(lambda x: x[1] == 'профессиональная', products))
    print(*proff_products, sep="\n")



products = [('Atache', 'профессиональная', 'очищение', 25),
            ('Atache', 'профессиональная', 'уход', 18),
            ('Atache', 'профессиональная', 'уход', 23),
            ('Atache', 'профессиональная', 'глаза', 12),
            ('Велиния', 'домашняя', 'уход', 8),
            ('Велиния', 'домашняя', 'очищение', 14),
            ('Велиния', 'домашняя', 'глаза', 19),
            ('Велиния', 'домашняя', 'крем', 21),
            ('G-Derm', 'профессиональная', 'уход', 35),
            ('G-Derm', 'профессиональная', 'уход', 41),
            ('G-Derm', 'профессиональная', 'очищение', 15),
            ('G-Derm', 'профессиональная', 'очищение', 28),
            ('ThaiTraditions', 'профессиональная', 'уход', 5),
            ('ThaiTraditions', 'профессиональная', 'уход', 7),
            ('ThaiTraditions', 'домашняя', 'крем', 6)]




