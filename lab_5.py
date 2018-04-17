def swap(A, i, j):
    if i != j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
    else:
        return -1

def part(A, first, last):
    start = first
    end = last
    mid = A[(first + last) // 2]

    while start < end:
        while A[start] > mid:
            start = start + 1
        while A[end] < mid:
            end = end - 1
        if start != end:
            swap(A, start, end)
    return A.index(mid)


def r_search(A, first, last, k):
    if first > last:
        return -1
    else:
        print(A)
        md = part(A, first, last)
        print("Middle element: ", A[md])
        print(A)
        print()
        if (md + 1 == k):
            return A[md]
        elif k < md + 1:
            # print("left find")
            return r_search(A, first, md, k)
        else:
            # print("right find")
            return r_search(A, md + 1, last, k)


if  __name__ == "__main__":
    n = int(input("Enter size of list: "))

    A = [2 * (x+1) for x in range(1, n + 1)]

    print('A =', A)

    pos = int(input("Enter pos maximum after: "))

    print(r_search(A, 0, len(A) - 1, pos))

    input("Press any key...")



