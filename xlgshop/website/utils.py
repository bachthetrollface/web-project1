class Cart:
    def __init__(self):
        self.item_list = dict()
    def calculate_price(self):
        result = 0
        for item in self.item_list.keys():
            result += item.price * self.item_list[item]
        return result
    def empty_cart(self):
        self.item_list.clear()
    def add_item(self, item):
        self.item_list[item] = self.item_list.get(item, 0) + 1
    def list_items(self):
        return self.item_list
    def remove_item(self, item):
        self.item_list.pop(item, 0)
    def update_amount(self, item, new_amount):
        if item not in self.item_list.keys():
            print("Item not found in cart!")
        else:
            self.item_list[item] = new_amount
    def get_amount(self, item):
        return self.item_list[item]