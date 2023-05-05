from lib.menu import Menu
from lib.menu_item import MenuItem
from lib.order import Order
from lib.confirmation import SendConfirmation

def test_add_menu_item():
    menu = Menu()
    menu_item = MenuItem('Meat', 55)
    menu_item.is_available = True
    menu.add_menu_item(menu_item)
    assert menu.menu_list == [menu_item]
def view_menu():
    menu = Menu()
    menu_item1 = MenuItem('Meat', 55)
    menu_item2 = MenuItem("Fish", 60)
    menu_item3 = MenuItem('Veggis', 70)
    menu_item3.mark_unavailable()    
    menu.add_menu_item(menu_item1)
    menu.add_menu_item(menu_item2)
    menu.add_menu_item(menu_item3)
    assert menu.view_menu == {'Meat': 55, "Fish":60}


def test_add_to_order():
    order = Order()
    menu_item = MenuItem('Meat', 55)
    menu_item_2 = MenuItem('Fish', 60)
    menu_item_3 = MenuItem('Veggis', 70)
    order.add_to_order(menu_item)
    order.add_to_order(menu_item_2)
    order.add_to_order(menu_item_3)
    order.add_to_order(menu_item)

    assert order.order_list == [menu_item, menu_item_2, menu_item_3, menu_item]

def test_view_order():
    order = Order()
    menu_item = MenuItem('Meat', 55)
    menu_item_2 = MenuItem('Fish', 60)
    menu_item_3 = MenuItem('Veggis', 70)
    order.add_to_order(menu_item)
    order.add_to_order(menu_item_2)
    order.add_to_order(menu_item_3)
    order.add_to_order(menu_item)

    assert order.view_my_order() == "Your final order is: Meat for 55$, Fish for 60$, Veggis for 70$, Meat for 55$ and the total: 240$"

def test_send_confirmation():
    send_confermation= SendConfirmation("4915158852831")
    
    assert send_confermation.send_confirmation_sms() == "Sent"