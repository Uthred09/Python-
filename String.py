print("Hello, there\'s hi \n how are you\"s ")

def printPicinic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth,'-'))
    for k , v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

picnicItems = {'Sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies':8000}

printPicinic(picnicItems, 12,5)

import pyperclip

pyperclip.copy('hello world')
pyperclip.paste()
