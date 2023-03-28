#! python3
# an insecure password locker program
import pyperclip
import sys

passwords = {
    'email': 'afbfajhfbaeu312546tuejhsfdc',
    'blog': 'ajkfjsdfbn43',
    'luggage': 'aajdsbfjafb52436t'
}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print('password for', account, 'copied to clipboard')
else:
    print("there is no account named", account)