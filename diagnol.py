def diagnollist1():
    numbers = []
    m = int(input("Enter the number of row: "))
    n = int(input("Enter the number of colums: "))

    for i in range(m):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            elif i < j:
                row.append(2)
            else:
                row.append(3)
                
        numbers.append(row)

    for row in numbers:
        print(row)

def calculate():
    