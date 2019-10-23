def quicksort(L, k):
    return q_sort(L, 0, len(L) - 1, k)


def q_sort(L, left, right, k):

    # if left <= right:
    pivot = Partition_left(L, left, right)
    # print(L[pivot])
    if k == pivot+1:
        # print(L[pivot],L)
        return L[pivot], L

    elif k < pivot+1:
        return q_sort(L, left, pivot - 1, k)

    else:
        return q_sort(L, pivot + 1, right, k)


        # q_sort(L, left, pivot - 1)
        # q_sort(L, pivot + 1, right)

    # return L


def Partition(L, left, right):


    if L[left] > L[right]:
        L[left],L[right]=L[right],L[left]
    if L[(left + right) // 2] < L[left]:
        L[left], L[(left + right) // 2]=L[(left + right) // 2],L[left]
    if L[(left + right) // 2] > L[right]:
        L[right], L[(left + right) // 2] = L[(left + right) // 2], L[right]



    if right-left > 2:
        key_inx = right - 1
        pivotkey = L[(left + right) // 2]
        L[(left + right) // 2] = L[key_inx]
        L[key_inx] = pivotkey


        right -=  2


        while left < right:
            while left <= right and L[right] >= pivotkey:
                right -= 1
            # L[left] = L[right]
            while left <= right and L[left] <= pivotkey:
                left += 1
            # L[right] = L[left]
            if left < right:
                L[left], L[right] = L[right], L[left]




        L[left], L[key_inx] = L[key_inx], L[left]
        # print(L)


    return left


# 若只取最左为基准
def Partition_left(L, left, right):

    pivotkey = L[left]

    while left < right:
        while left < right and L[right]>=pivotkey:
            right-=1
        L[left] = L[right]
        while left < right and L[left]<=pivotkey:
            left+=1
        L[right] = L[left]

    L[left] = pivotkey

    return left

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[int(len(arr) / 2)]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)
#
# import random
# L = []
# for i in range(1000):
#     L.append(random.randint(1,100))
#
# print(L)
# L = [7,67,89,100,3,4,1,29,83,2,10,9,57,81,13]
L = [10,12,13,6,9,2,5,1]

print(quicksort(L, 6))
