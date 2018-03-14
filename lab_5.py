import random
def max_after(list, pos):
    for i in range(pos):
        max_pos = 0
        for j in range(len(list)-i):
            if list[ max_pos] < list[j]:
                 max_pos = j
        if list[ max_pos] != list[len(list)-1-i]:
            temp = list[n-1-i]
            list[len(list)-1-i] = list[ max_pos]
            list[ max_pos] = temp
    return list[len(list)-pos]

n = int(input("Input size of list: "))
list = [int(random.random()*10) for x in range(1,n+1)]
print(list)
position = int(input("Input position: "))
print(max_after(list, position))
print(list)
