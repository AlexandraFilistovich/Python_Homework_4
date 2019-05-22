import random


x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e',
     'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
     'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E',
     'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
     'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

while (1):
    print('Enter length of password:')
    s = str(input())
    if s == '0':
        break
    if s.isdigit() == 0:
        print('Not a digit.')
        continue
    print('Password:', end='')
    for i in range(int(s)):
        print(random.choice(x), end='')
    print()
