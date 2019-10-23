# 给出一个01串，给出0和1数目相等的最长子串的长度。比如’00100110011’的最长字串的长度为10
# 普通算法
import  os, sys
#
#
# def find(l1):
#     l2 = []
#     for i in range(len(l1)):
#         n1 = 0
#         n2 = 0
#         for j in range(i, len(l1)):
#             if l1[j] == 0:
#                 n1 = n1 + 1
#             else:
#                 n2 = n2 + 1
#
#             if n1 == n2:
#                 l2.append(n1+n2)
#
#     if l2 == []:
#         print(0)
#     else:
#         return max(l2)
#
# if __name__ == '__main__':
#
#     l1 = []
#     print("please input:")
#     while True:
#         line = sys.stdin.readline().strip()
#         if line == '':
#             break
#         s = map(int,line)
#         print(s)
#         l1 = list(map(int, line))
#
#
#     print(l1)

    #
    # print(find(l1))

# 动态规划解法
def longlen01str(nums):
    count = [0, 0] #记录0，1分别的个数
    A = [0 for i in range(len(nums))] #构造数组记录0，1个数的差值
    dic = {} # 记录A中某个值第一次出现的索引值
    longest = 0
    for i in range(len(nums)):
        count[nums[i]] += 1
        A[i] = count[0]-count[1]
        if A[i] == 0:
            longest = i+1
        if A[i] in dic:
            longest = max(longest, i - dic[A[i]])
        else:
            dic[A[i]] = i

    return longest
#
# nums=[1,0,0,1,0,1,1,0]
# nums = [1,0,1,1,0,1,0]
# print(longlen01str(nums))

# 2. 给定一个字符串，请你找出其中不含有重复字符的 最长子串的长度。
def longlenrepstr(l):
    longest = 0
    left = 0 # 合法位置，跳过重复的元素
    dic = {}
    for i in range(len(l)):
        if l[i] in dic and dic[l[i]]>=left:
            left = dic[l[i]]+1

        dic[l[i]] = i

    longest = max(longest, i-left+1)
    return longest

# s = 'pwwkew'
# l = list(s)
# print(l)
# print(longlenrepstr(l))


# 3. 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入股票前卖出股票。

def stock(nums):
    minimum = nums[0]
    profit = 0

    for i in nums:
        minimum = min(i, minimum)
        profit = max(i-minimum, profit)

    return profit

# 4. House Robber 从数组中找出一个或多个不相邻的数，使其和最大。

def houserobber(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = max(nums[1], dp[0])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])

    return dp[-1]

nums = [1,2,3,1,5,1,6,1,1,7]

print(houserobber(nums))