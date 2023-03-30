# table = [['apples', 'banana', 'cherries', 'oranges'],
#          ['Alice', 'Bob', 'carol', 'david'],
#          ['dogs', 'cats', 'Moose', 'goose']
#          ]

# def printTables(ls):
#     for i in range(len(ls)):
#         for j in range(len(ls[i])):
#             print(ls[i][j])

# printTables(table)

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
