import sys
# 从1到n整数中1出现的次数 e.g. 6543 分某一位等于0或1或大于1的情况

def count1str(str):
    n = int(str)
    round = n
    base = 1
    count = 0

    while(round > 0):
        reminder = round % 10
        round = int(round / 10)
        count += round * base

        if reminder == 1:
            count += (n%base) + 1
        if reminder > 1:
            count += base

        print(count)

        base = base*10

    return count

# 把数组中的数排成最小数
# 主要是定义一个新的排列的规则
def number_smallest(arr):
    if not arr:
        return ""
    arr = list(map(str, arr))
    pivot = arr[0]
    left = [i for i in arr[1:] if pivot+i>i+pivot]
    right = [i for i in arr[1:] if pivot+i<=i+pivot]

    result = "".join(number_smallest(left))+pivot+"".join(number_smallest(right))

    return result

# 调整数组顺序使奇数位于偶数前面
def sort_odd_even(arr):
    left = 0
    right = len(arr)-1

    while left<right:
        while left<right and arr[left]%2!= 0:
            left+=1
        while left<right and arr[right]%2 == 0:
            right-=1

        arr[left], arr[right] = arr[right], arr[left]

    return arr

# 要求奇数和偶数相对位置不变
def reorder_odd(array):
    for i in range(1, len(array)):
        if array[i] % 2 == 1:
            for j in range(i, 0, -1):
                if array[j-1]%2 == 0:
                    array[j], array[j-1] = array[j-1], array[j]

    return array

# 数字在排序的数组中出现的次数

#找到第一次出现的k
def getfirstK(arr, k, low, high):

    while low<=high:
        mid = (low+high)//2
        if arr[mid] == k:
            if mid-1>=0 and arr[mid-1] == k:
                high = mid-1
            else:
                return mid
        elif arr[mid]<k:
            low = mid+1
        else:
            high = mid-1


def getlastK(arr, k, low, high):

    while low <= high:
        mid = (low + high) // 2
        print(low, high, mid)
        if arr[mid] == k:
            if mid+1<len(arr) and arr[mid + 1] == k:
                low = mid+1
            else:
                return mid
        elif arr[mid] < k:
            low = mid+1
        else:
            high = mid-1


def countK(arr, k):
    arr = arr
    k = k
    low = 0
    high = len(arr) - 1
    first = getfirstK(arr, k, low, high)
    last = getlastK(arr, k, low, high)
    count = last-first+1

    return count

#一个数组，除了一个数出现次数为1，其他数的出现次数都为2，找到出现一次的那个数

#找到第N个丑数
#丑数为除1以外，2，3，5的倍数
def minimum(a, b, c):
    if a>b:
        a, b = b, a
    if a>c:
        a, c = c, a

    return a


def uglynumber(n):
    ugly_numbers = []
    ugly_numbers.append(1)

    number2 = ugly_numbers[0]
    number3 = ugly_numbers[0]
    number5 = ugly_numbers[0]

    next_index = 1

    while next_index < n:
        min = minimum(number2*2, number3*3, number5*5)
        ugly_numbers.append(min)

        while number2*2 <= min:
            number2+=1
        while number3*3 <= min:
            number3+=1
        while number5*5 <= min:
            number5+=1

        next_index+=1

    ugly = ugly_numbers[-1]
    print(ugly_numbers)

    return ugly




import numpy as np
arr = np.array([[1,2],[4,5],[7,8]])
a = arr.mean(axis=1)
print(a)
# s = '21345'
# arr = [1,2,3,3,3,3,3,4,5,6,6,6,6,6,6,6,6,6]
# print(uglynumber(15))
# # print(count1str(str))
# print(countK(arr,6))
