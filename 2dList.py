table = [['apples', 'banana', 'cherries', 'oranges'],
         ['Alice', 'Bob', 'carol', 'david'],
         ['dogs', 'cats', 'Moose', 'goose']
         ]

def printTables(ls):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            print(ls[i][j])

printTables(table)