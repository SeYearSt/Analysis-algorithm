def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    else:
        return binary_search_recursive(arr, elem, mid+1, end)
    
n = int(input("Input size of list: "))
list = [x for x in range(1,n+1)]
print(list)
x = int(input("Input number for finding: "))
binary_search_recursive(list,x)
print(list[binary_search_recursive(list,x)])
