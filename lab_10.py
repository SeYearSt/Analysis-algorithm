import numpy as np

sizes = (min, max) = (2, 5)
number = 10

a = np.random.randint(min, max)
b = np.random.randint(min, max)
c = np.random.randint(min, max)

A = np.random.randint(number, size=(a, b))
B = np.random.randint(number, size=(b, c))
C = np.zeros((a,c));

d = b // 2

row_factor = []
for i in range(a):
    row_factor.append(A[i][0]*A[i][1])
    for j in range(1, d):
        row_factor[i] += A[i][2*j]*A[i][2*j+1]

column_factor = []
for i in range(b):
    column_factor.append(B[0][i]*B[1][i])
    for j in range(1, d):
        column_factor[i] += B[2*j][i]*B[2*j+1][i]

for i in range(a):
    for j in range(c):
        C[i][j] -= row_factor[i] + column_factor[j]
        for k in range(d):
            C[i][j] += (A[i][2*k+1]+B[2*k][j])*(A[i][2*k]+B[2*k+1][j])

if b%2 != 0:
    for i in range(a):
        for j in range(c):
            C[i][j] += A[i][b-1] * B[b-1][j]



print("Row Factor:", row_factor)
print("Column Factor", column_factor)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Result Matrix:")
print(C)