from lib.order import Order
from unittest.mock import Mock

def test_add_to_order():
    order = Order()
    item = Mock()
    item.name.return_value = "Meat"
    item.price.return_value = 55
    order.add_to_order(item)
    assert order.order_list == [item]
def test_view_my_order():
    order = Order()
    item_1 = Mock()
    item_2 = Mock()
    item_1.name = "Meat"
    item_1.price = 55
    item_2.name= "Fish"
    item_2.price = 60  
    order.add_to_order(item_1)
    order.add_to_order(item_2)
    order.add_to_order(item_1)
    assert order.view_my_order() == "Your final order is: Meat for 55$, Fish for 60$, Meat for 55$ and the total: 170$"  