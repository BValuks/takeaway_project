class Menu:
    def __init__(self):
        self.items_sold = {}
        self.menu_items = {
            'Burgers': [
                {'Cheeseburger': {'Price': 10.00, 'Stock count': 5}},
                {'Pulled Pork Burger': {'Price': 12.00, 'Stock count': 0}},
                {'Chicken Burger': {'Price': 10.50, 'Stock count': 5}},
                {'Halloumi Burger': {'Price': 9.00, 'Stock count': 4}},
                {'Jackfruit Burger': {'Price': 9.50, 'Stock count': 3}}
            ],
            'Sides': [
                {'Onion Rings': {'Price': 6.00, 'Stock count': 10}},
                {'Skin-on-fries': {'Price': 4.00, 'Stock count': 25}},
                {'Chilli Cheese Bites': {'Price': 6.50, 'Stock count': 8}},
                {'Side Salad': {'Price': 4.00, 'Stock count': 20}}
            ],
            'Drinks': [
                {'Coke': {'Price': 2.40, 'Stock count': 24}},
                {'Water': {'Price': 2.00, 'Stock count': 18}},
                {'Beer': {'Price': 5.25, 'Stock count': 24}}
            ]
        }
    
    def formatted_menu(self):
        formatted_menu = 'Menu items:'
        for submenu in self.menu_items.items():
            formatted_menu += f'\n\n * {submenu[0]}| '
            for i in range(len(submenu[1])):
                for menu_item in submenu[1][i].items():
                    figures = list(menu_item[1].items())
                    formatted_menu += f'\n - {menu_item[0]}, Price: {figures[0][1]}, Available: {figures[1][1]} '
        return formatted_menu
    
    def popular_items(self):
        output_string = 'Top items: \n'
        sorted_items = sorted(self.items_sold.items(), key=lambda item: item[1], reverse=True)
        if len(sorted_items) > 3:
            for i in range(3):
                output_string += f'{i + 1}. {sorted_items[i][0]}\n'
        return output_string

    def view_items_sold(self):
        return self.items_sold

    def reset_items_sold(self):
        self.items_sold = {}
        return 'Items sold reset'