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
# first a list is iterated and check which each element at indix if the condition satisfied a newiteam value is increased,
#then, olditem value and new item value added to make total item,finally the dictionary value is updated with total iteam 
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
