print('Enter string:')
s = str(input())
sw = s.split()
l = len(sw)

for i in range(l):
    ls = len(sw[i])
    for j in range(ls):
        print(sw[i][ls-1-j], end='')
    print(' ', end='')
