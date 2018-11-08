def displayInventory(inventory):
    # Function to display items in the inventory 
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        print(v, k)
        total_items += v
    print("Total number of items: {0}".format(total_items))

def addToInventory(inventory, addedItems):
    # Function for updating the dictionary inventory with a list
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory
stuff =  {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'rope', 'ruby']

displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
