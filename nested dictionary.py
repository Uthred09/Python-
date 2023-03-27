# dic = {'brand': 'ford', 'price': 50000, 'Model': 'Mustang'}

# for i , j in dic.items():
#     print(i,j)

# # nested dic

# dic = {
#     'child1': {'name' : 'hemanta', 'age': 10, 'grade': 5},
#     'child2' : {'name': 'lawang', 'age': 9, 'grade': 5},
#     'child3' :{'name': 'sairus', 'age': 10, 'grade': 10}
# }

# print(dic['child1']['name'])

# for i, j in dic.items():
#     # print(dic['child1'].get('name'))
#     print(i,j)

# for i in dic.values():
#     print(i)

# for j in dic.keys():
#     print(j)


allguest = {'alice': {'apples': 5, 'pretzels': 12},
            'bob': {'ham sandiwiches': 3, 'apples':2},
            'Carol':{'cups': 3, 'apples pies': 1}
            }

numbrought = 0
for i, j in allguest.items():
    numbrought = j.get('apples', 0) + numbrought
print(numbrought)

# using function

def totalbrought(guest, item):
    numbroughts = 0
    for i, j in guest.items():
        numbroughts = numbroughts + j.get(item, 0)
    return numbroughts

print(totalbrought(allguest, 'apples'))