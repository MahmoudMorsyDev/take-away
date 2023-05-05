class Order:
    def __init__(self):
        '''
        Properties:
            Order_list: List of instance of the menu items that was ordered
        Parameters:
            nothing
        '''
        self.order_list = []
    def add_to_order(self, item):
        '''
        Parameters:
            item: an instance of the menu item
        Returns:
            Nothing
        Side Effects:
            adds an item to the list of order                
        '''
        if item.is_available:
            self.order_list.append(item)    
    def view_my_order(self):
        '''
        Parameters:
            Nothing
        Returns:
            returns a list of items names, count and thier price with the total amount 
        Side Effects:
            None              
        '''
        total_price = sum(item.price for item in self.order_list)
        order_items = []
        for item in self.order_list:
            count = self.order_list.count(item)
            order_items.append(f'{item.name} for {item.price}$')
        order_summary =  ", ".join(order_items)
        the_result = f"Your final order is: {order_summary} and the total: {total_price}$"
        print(the_result)
        return the_result
