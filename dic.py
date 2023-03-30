user = 'y'
while user == "y":
    dic = {'Name':{'English': '','Science':' ', 'math':''}}
    name = input("Enter Name of student: ")
    eng_mark = int(input("Enter marks of English: "))
    sci_mark = int(input("Enter marks of Science: "))
    math_mark = int(input("Enter marks of Math: "))
    dic['Name']= [name]
    dic['English'] = [eng_mark]
    dic['Science'] = [sci_mark]
    dic['Math'] = [math_mark]
    print(dic['Name'])
    print(dic['English'])
    print(dic['Science'])
    print(dic['Math'])

    user = input("do you want to coninue[y/n]?:  ")
