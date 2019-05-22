print('Enter string:')
s = str(input())
l = len(s)
b = 1

for i in range(l//2):
    if (s[i] != s[l-1-i]):
        b = 0
        break
if b:
    print('Srting is a palindrome.')
else:
    print('Srting is NOT a palindrome.')