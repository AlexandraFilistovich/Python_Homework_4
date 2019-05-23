from collections import Counter


l = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]

#1.1
print('=====1.1=====')
print('Min:', min(l), ', index of min:', l.index(min(l)))
print('Max:', max(l), ', index of max:', l.index(max(l)))

#1.2
print('=====1.2=====')
count = Counter(l)
print('Most common elements:', count.most_common()[0][0], count.most_common()[1][0],count.most_common()[2][0])

#1.3.1
print('=====1.3.1=====')
l.sort()
newl = [l[0]]
for i in range(1, len(l)):
    if l[i] != l[i - 1]:
        newl.append(l[i])
print('Massive without repeat: ', newl)

#1.3.2
l = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
print('=====1.3.2=====')
newl = []
for i in range(len(l)):
    if (l[i] in newl) == False:
        newl.append(l[i])
print('Massive without repeat (same order): ', newl)
