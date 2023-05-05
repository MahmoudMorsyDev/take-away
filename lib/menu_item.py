class MenuItem:
    def __init__(self, name, price):
        '''
        Parameters:
            name: the name of the item
            price: the price of the item
        Properties:
            name: the name of the item
            price: the price of the item
            is_available: True if the item is currently available false if not
        '''   
        self.name = name
        self.price = price
        self.is_available = True
    def mark_unavailable(self):
        '''
        Parameters:
            Nothing
        Returns:
            Nothing    
        Side Effects:
            Changes the Is_available to False
        '''
        self.is_available = False 
    def mark_available(self):
        '''
        Parameters:
            Nothing
        Returns:
            Nothing    
        Side Effects:
            Changes the Is_available to False    
        '''
        self.is_available = True