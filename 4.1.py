'''1. Дан массив. Реализовать функцию которая будет переставлять 2 выбранных элемента списка местами. Функция должна иметь вид:
def swap(target_list, item_index1, item_index2).'''

def swaping(l, i1, i2):
    c = l[i1]
    l[i1] = l[i2]
    l[i2] = c
    return l


x = [1, 2, 3, 4, 5]
swaping(x, 1, 3)
print(x)