from lib.menu_item import MenuItem

def test_menu_item():
    menu_item = MenuItem("Meat", 55)
    assert menu_item.price == 55
    assert menu_item.is_available == True

def test_mark_unavailable():    
    menu_item = MenuItem("Meat", 55)
    menu_item_2 = MenuItem("Fish", 60)
    menu_item_2.mark_unavailable()
    assert menu_item.is_available == True
    assert menu_item_2.is_available == False

def test_mark_available():
    menu_item = MenuItem("Meat", 55)
    menu_item_2 = MenuItem("Fish", 60)
    menu_item_2.mark_unavailable()
    assert menu_item_2.is_available == False
    menu_item_2.mark_available()
    assert menu_item_2.is_available == True
