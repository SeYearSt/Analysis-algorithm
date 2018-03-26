import random

def insertion_sort(A):
    for j in range(1,len(A)):
        temp = A[j]
        i = j - 1
        while (i>= 0 and A[i] > temp):
            A[i+1] = A[i]
            A[i] = temp
            i=i - 1
    
def main():
    size = int(input("Etner size of list: "))
    A = [int(random.random()*10) for i in range(size)]
    print("A =",A)
    insertion_sort(A)
    print("A =",A)
