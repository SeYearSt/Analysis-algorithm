A = [9,1,3,4,5,11,10,12]
print('A =',A)

def sort(A,index):
    left_list = []
    right_list = []
    main_list = []
    
    main_element = A[index]
    left_list = [x for x in A if x > A[index]]
    right_list = [x for x in A if x < A[index]]
    
    main_list.extend(left_list)
    main_list.append(main_element)
    main_list.extend(right_list)
    
    A[:] = main_list[:]
    return A.index(main_element)

def get_max_after(A,p):
    k = sort(A,0)
    while True:
        if k == p:
            return A[k]
        elif k < p:
            k = sort(A,k+1)
        else: #k > p
            k = sort(A,0)
    print(A[k])
 