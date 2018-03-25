from random import * 
w, h = 3, 3;
matrix = [[random() for x in range (w)] for y in range (h)]
minsInRows = []
for i in range (h):
    print(matrix[i])
for i in range (h):
    for j in range(w):
        if j == 0:
            min = matrix[i][j]
        elif min > matrix[i][j]:
            min = matrix[i][j]
    minsInRows.append(min)
print("Mins")
print(minsInRows)
max = minsInRows[0]
for i in range(len(minsInRows)):
    if max < minsInRows[i]:
        max = minsInRows[i]
print("Max in mins is:",max)
