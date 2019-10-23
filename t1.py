# 给出一个01串，给出0和1数目相等的最长子串的长度。比如’00100110011’的最长字串的长度为10
# import  os, sys
#
#
# def find(l1,l2):
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

    # l2 = []
    #
    # print(find(l1, l2))


import sys
import re

# if __name__ == "__main__":
#
#     l=[]
#
#     while True:
#         line = sys.stdin.readline().strip()
#         if line == '':
#             break
#
#     #     a = line.split(',')
#     #     b = a[-1].split(';')
#         a = re.split(r'[,;]', line)
#         l.append(list(map(int,a)))
#
#         # a = a.split(';')
#
#     print(l)
    # print(b)

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

def alarmtrick(s, nums):
    left = 0
    sum = 0
    longest = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum > s:
            sum -= nums[left]
            left = left+1


        longest = max(longest, i-left+1)



    return longest



L = []

while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    a = list(map(int, line.split()))
    L.append(a)

s = L[0][1]
nums = L[1]
print(alarmtrick(s, nums))

# 替换空格

def replaceblank(s):
    ori_length = len(nums)
    n = 0
    for c in s:
        if c == ' ':
            n+=1

    length = ori_length+n*2



