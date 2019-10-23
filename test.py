# import sys
# import re
# # def operation(n):
# #     op = 0
# #     if n == 0:
# #         return 1
# #     if n == 1:
# #         return 0
# #
# #     while(n!= 1):
# #         if n%3 == 0:
# #             n = n/3
# #         elif n%2 == 0:
# #             n = n/2
# #         else:
# #             n += 1
# #         op+=1
# #
# #     return op
# #
# #
# # number = sys.stdin.readline().strip()
# # n = int(number)
# # print(operation(n))
#
# # def quick_sort(a, left, right, k):
# #
# #       return q_sort(a, left, right, k)
# #
# # def q_sort(L, left, right, k):
# #     if left < right:
# #         pivot = Partition_left(L, left, right)
# #         print(pivot)
# #         if k == pivot+1:
# #             return L[pivot], L
# #         if k < pivot+1:
# #
# #             return q_sort(L, left, pivot - 1, k)
# #
# #         else:
# #             return q_sort(L, pivot + 1, right, k)
# #
# # def Partition_left(L, left, right):
# #     pivotkey = L[left]
# #
# #     while left < right:
# #         while left < right and L[right]>=pivotkey:
# #             right-=1
# #         L[left] = L[right]
# #         while left < right and L[left]<=pivotkey:
# #             left+=1
# #         L[right] = L[left]
# #
# #     L[left] = pivotkey
#
# #     return left
# #
# # nums=[10,12,13,6,9,2,5,1]
# # quick_sort(nums,0,7,5)
#
#
# # def candy(n, m, a, nums):
# #     record = [1 for i in range(n)]
# #     for i in range(m):
# #         left = nums[i][0]-1
# #         right = nums[i][1]
# #         for j in record[left: right]:
# #             if j == 0:
# #                 left+=1
# #         if left <= right:
# #             return -1
# #         k_val, a = quick_sort(a, left, right, nums[i][2])
# #         record[nums[i][0]-1:nums[i][2]] = 0
# #         print(k_val)
# #
# # l = []
# # while True:
# #     line = sys.stdin.readline().strip()
# #     if line == '':
# #         break
# #     line = list(map(int, line.split()))
# #     l.append(line)
# #
# # n = l[0][0]
# # m = l[0][1]
# # a = l[1]
# # nums = l[2:]
# # candy(n,m,a,nums)
#
# def concat(nums1, nums2):
#     new_nums = []
#     # if nums1[-1] == '' and nums2[0] == '':
#     #     new_nums = '/'
#
#     if nums1[-1] != '/' and nums2[0] != '/':
#         new_nums = nums1+['/']+nums2
#
#     elif nums1[-1] == '/' and nums2[0] == '/':
#         new_nums = nums1[:-1]+nums2
#
#     else:
#         new_nums = nums1 + nums2
#
#     return "".join(new_nums)
#
# def biggest_profit(nums):
#     l = len(nums)
#     dp = [1 for i in range(l)]
#     count = 0
#     new_nums = [[] for i in range(l)]
#     result = []
#     for i in range(1,l):
#         for j in range(0, i):
#             if nums[j][1]<=nums[i][0]:
#                 if dp[i] == dp[j]+1:
#                     if nums[j][1]<new_nums[i][-1][1]:
#                         new_nums[i][-1] = nums[j]
#                     elif nums[j][1] == new_nums[i][-1][1]:
#                         if nums[j][0]>new_nums[i][-1][0]:
#                             new_nums[i][-1] = nums[j]
#                 elif dp[j]+1>dp[i]:
#                     dp[i] = dp[j]+1
#                     new_nums[i].append(nums[j])
#                     # print(new_nums[i])
#                 # else:
#                 #     dp[i] = dp[i]
#
#         if count < dp[i]:
#             count = dp[i]
#             result = new_nums[i]
#             result.append(nums[i])
#         elif count == dp[i]:
#             if result[-1][1]>nums[i][1]:
#                 result[-1] = nums[i]
#             elif result[-1][1] == nums[i][1]:
#                 if result[-1][0] < nums[i][0]:
#                     result[-1] = nums[i]
#
#
#
#
#     return count, result
#
#
#
#          # m = max(m, dp[i])
#
#
# # line = sys.stdin.readline().strip()
# #
# # l = list(line.split(","))
# #
# # print(line)
# #
# # if l==['',''] or l == ['']:
# #     nums1 = ['']
# #     nums2 = ['']
# # else:
# #     nums1 = list(l[0])
# #     nums2 = list(l[1])
# #
# # print(concat(nums1,nums2))
#
# line = sys.stdin.readline().strip()
#
#
# l1 = list(line.split(" "))
# l2 = []
# for num in l1:
#     nums = re.findall('\d+', num)
#     l2.append(tuple(list(map(int,nums))))
# print(l2)
# max_profit, arr = biggest_profit(l2)
# print("count:"+str(max_profit))
# # result = " ".join(arr)
#
#
# print(arr)
#

def max_length(n):
    # if n = 1:
    #     return 3
    record = [3,3]
    a=3
    b=3
    l = 0
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        record.append(c)
    while record:
        dist = record.pop()
        l=2*(l+dist)

    return l


import sys
n = sys.stdin.readline().strip()
print(max_length(int(n)))
