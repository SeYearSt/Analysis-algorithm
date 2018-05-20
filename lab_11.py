import numpy as np

def DFS(A, k):
    A[k][k] = 1
    print(k, end=' ')
    for j in range(len(A)):
        if A[k][j] == 1 and A[j][j] != 1:
            DFS(A, j)

def BFS(A,k):
   A[k,k] = 1
   start = 0
   B = []
   B.append(k)
   end = start
   while start <= end:
       k = B[start]
       for j in range(len(A)):
           if A[k][j] == 1 and A[j][j] != 1:
               A[j][j] = 1
               B.append(j)
               end += 1
       start += 1
   print(B)
if __name__ == "__main__":

    n = int(input('Input count of nodes: '))

    graph = np.random.randint(0, 2, size = (n,n))

    for i in range(len(graph)):
        graph[i][i] = 0

    print('Graph :\n', graph)


    node_number = int(input('Input number node`s number: '))

    print("DFS: ", end= '')
    DFS(graph, node_number)
    print()

    for i in range(len(graph)):
        graph[i][i] = 0

    #print('Graph :\n', graph)

    print("BFS: ", end='')
    BFS(graph, node_number)

    input("End")
