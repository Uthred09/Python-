allguest = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups':3, 'apple pie':1}
            }

def totalBrought(guest, item):
    numBrought = 0
    for i, j in guest.items():
        numBrought = numBrought + j.get(item, 0)
        return numBrought

print('Number of things being Brought: ')
print('Apples', totalBrought(allguest, 'apples'))
print("pretzels", totalBrought(allguest, 'pretzels'))
print('ham sandwiches', totalBrought(allguest, 'ham sandwiches'))