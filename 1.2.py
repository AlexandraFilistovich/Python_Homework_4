a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

# 2.1
print('=====2.1=====')
print('Same keys:', end=' ')
for key in a:
    for jey in b:
        if key == jey:
            print(key, end=' ')
print()

# 2.2
print('=====2.2=====')
print('Keys that exist only in second dict:', end=' ')
for key in b:
    f = 1
    for jey in a:
        if key == jey:
            f = 0
    if f:
        print(key, end=' ')
print()

# 2.3
print('=====2.3=====')
c = a.copy()
for key in b:
    if (key in c.keys()) == False:
        c[key] = b[key]
    else:
        c[key] += b[key]
print('New dict:', c)
