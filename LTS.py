import sys

# 投票选举
# def vote(nums, k):
#     n = len(nums)
#     candidate = []
#     for i in range(n):
#         if nums[i] in candidate:
#             continue
#         candidate.append(nums[i])
#         v = 0
#         for j in range(i, n):
#             if nums[j] == nums[i]:
#                 v += 1
#         if v > (n/k):
#             return nums[i]

#拆迁房子 8 2 3 1 4 4 输出 2
#第一个数字表示长度为8
# def house(s, nums):
#     n = len(nums)
#
#     L = []
#     for i in range(n):
#         m = 0
#         sum = 0
#         for j in range(i, n):
#             sum += nums[j]
#             m += 1
#             if sum >= s:
#                 L.append(m)
#                 break
#     if L == []:
#         return 0
#
#     return min(L)
#
def alarmtrick(s, nums):
    length = []
    for i in range(len(nums)):
        count = 0
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            count += 1
            if sum > s:
                length.append(count)
                break
    if length == []:
        return 0

    return min(length)
# line = sys.stdin.readline().strip()
# L = list(map(int, line.split()))
#
# k = L[0]
# nums =  L[1:]
# print(vote(nums,k))

# 求最大子数组和
def longarraysum(nums):
    l = len(nums)
    dp = [x for x in nums]

    for i in range(1,l):
        dp[i] = max(dp[i-1]+nums[i],dp[i])

    return max(dp)



# 求最长升序子序列
def LTS(nums):
    l = len(nums)
    m = 0
    dp = [1 for i in range(l)]
    for i in range(1, l):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j]+1, dp[i])

        m = max(dp[i], m)

    return m

# line = sys.stdin.readline().strip()
# nums = list(map(int, line.split()))
#
# print(LTS(nums))

nums = [1,-2,3,10,-4,7,2,-5]
print(longarraysum(nums))