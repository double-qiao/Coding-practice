# 归并排序

def mergesort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums) // 2
    l1 = mergesort(nums[:mid])
    l2 = mergesort(nums[mid:])

    return merge(l1,l2)

def merge(l1, l2):
    i = 0
    j = 0
    new_nums = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            new_nums.append(l1[i])
            i+=1
        else:
            new_nums.append(l2[j])
            j+=1

    new_nums+=l1[i:]
    new_nums+=l2[j:]

    return new_nums

# bubble sort

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[j]<nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]

    return nums

# insert sort
def insert_sort(nums):
    for i in range(1,len(nums)):
        for j in range(0, i):
            if nums[i] < nums[j]:
                nums[j],nums[i] = nums[i],nums[j]

    return nums

nums = [2,6,7,8,10,11,3,14,9,18,1]
# print(mergesort(nums))
print(bubble_sort(nums))


