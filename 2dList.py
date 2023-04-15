# table = [['apples', 'banana', 'cherries', 'oranges'],
#          ['Alice', 'Bob', 'carol', 'david'],
#          ['dogs', 'cats', 'Moose', 'goose']
#          ]

# def printTables(ls):
#     for i in range(len(ls)):
#         for j in range(len(ls[i])):
#             print(ls[i][j])

# printTables(table)
def example():
    A = [[102,56, 98],
        [150, 98, 18],
        [2, 66, 7]]

    max_ = A[0][0]
    min_ = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] % 2 == 0 and A[i][j] % 3 == 0: 
                print(A[i][j])
            if  max_ < A[i][j]:
                max_ = A[i][j] 
            if min_ > A[i][j]:
                min_ = A[i][j]

    print("The maximum num is",max_)
    print("the minimum num is",min_)

def list_():

    loop = True
    main_ = []
    child_list= []
    while loop == True:
        
        brand = input("laptop Brand: ")
        product = input("Laptop Model: ")
        quantity = int(input("Quantity: "))
        price = int (input("Price: "))
        child_list.append(brand)    
        child_list.append(product)
        child_list.append(quantity)
        child_list.append(price)

        main_.append(child_list)
        user = input("do you want to continue:")
        if user == 'y':
            child_list = []
            loop = True
        else:
            return main_

def print_():
    main = list_()
    for i in range(len(main)):
        print(main[i][j])

A = [[102,56, 98],
    [150, 98, 18],
    [2, 66, 7]]

for i in range(len(A)):
    print(A[i])
    for j in range(len(A[i])):
       print(A[i][j], A[i][j+1], A[i][j+2])
       break

        