inventory = {'rope': 1, 'torch': 6, 'goldcoin': 42, 'dagger' : 1,'arrow': 12 }

def displayInventory(dic):
    print("Inventory: ")
    totalItems = 0
    for i , j in dic.items():
        print(j, i)
        totalItems = totalItems + j
    print(totalItems)

# displayInventory(inventory)

dragonLoot = ['goldcoin' , 'goldcoin' , 'ruby']

def addToInventory(inventory, addedItems):
    newItem = 0
    for i in range(len(addedItems)):
        if addedItems[i] == 'goldcoin':
            newItem += 1 
    totalItem = inventory.get('goldcoin') + newItem
    inventory.update({"goldcoin": totalItem})
    return inventory

inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)
