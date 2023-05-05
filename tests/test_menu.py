from lib.menu import Menu
from unittest.mock import Mock
def test_add_menu_item():
    menu = Menu()
    new_dish = Mock()
    menu.add_menu_item(new_dish)
    assert menu.menu_list == [new_dish]

def test_view_menu():
    menu = Menu()
    new_dish1 = Mock()
    new_dish2 = Mock()
    new_dish1.name = 'Meat'
    new_dish1.price = 55
    new_dish2.name= 'Fish'
    new_dish2.price= 60
    menu.add_menu_item(new_dish1)
    menu.add_menu_item(new_dish2)
    assert menu.view_menu() == {"Meat":55, "Fish":60}
