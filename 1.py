from collections import Counter


l = 'spam and eggs or eggs with spam'

count = Counter(l)

for i in range(len(count.most_common())):
    print('Symbol:', count.most_common()[i][0], 'Amount of symbol:', count.most_common()[i][1])
