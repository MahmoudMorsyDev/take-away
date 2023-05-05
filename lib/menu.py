class Menu:
    def __init__(self):
        '''
        Properties:
            menu_list: a list of available dishes 
        '''
        self.menu_list = []
    def add_menu_item(self, item):
        '''
        Parameters:
            item: an instance of a menu item
        Returns:
            Nothing
        Side Effects:
            adds an item to the menu list if available       
        '''
        if item.is_available:
            if item not in self.menu_list:
                self.menu_list.append(item)
    def view_menu(self):
        '''
        Parameters:
            Nothing
        Returns:
            returns a list of available items names and thier prices
        Side_Effects:
            Nothing    
        '''    
        for item in self.menu_list:
            print(item.name)
            print(item.price)
        return {item.name: item.price for item in self.menu_list}
