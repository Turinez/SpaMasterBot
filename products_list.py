def sort_key(e):
    return e[3]
def to_string(product_list):

    return f"Косметика {str(product_list[1])} фирмы {str(product_list[0])} стоимостью {str(product_list[3])} рублей"

def search():
    sorted_products = sorted(products, key=sort_key)
    to_print = sorted_products[0:10]
    return to_print




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




