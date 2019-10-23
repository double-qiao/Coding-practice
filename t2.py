# 给定一个长度为N-1且只包含0和1的序列A1到AN-1，如果一个1到N的排列P1到PN满足对于1≤i<N，当Ai=0时Pi<Pi+1，当Ai=1时Pi>Pi+1，则称该排列符合要求，那么有多少个符合要求的排列？

# 找两个字符串的最长公共子串
# abcdefg, abcfbng
import sys


def findlongcom(l1, l2):
    rec = [[0] * (len(l1)) for i in range(len(l2))]
    m = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                if i == 0 or j == 0:
                    rec[i][j] = 1
                else:
                    rec[i][j] = 1 + rec[i - 1][j - 1]

                m = max(rec[i][j], m)

    return m

#
# l = []
# while True:
#     line = sys.stdin.readline().strip()
#     if line == '':
#         break
#
#     l.append(list(''.join(line.split())))
#
# print(l)
# m = findlongcom(l[0], l[1])
# print(m)

# 一只青蛙要跳上n层高的台阶，一次能跳一级，也可以跳两级，请问这只青蛙有多少种跳上这个n层高台阶的方法？
# 递推公式 f(n)=f(n-1)+f(n-2)
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
        a=1;b=2;c=3
        for i in range(3,n+1):
            c=a+b;a=b;b=c
        return c

# 顺时针打印矩阵
def array_print(nums):
    up_row = 0
    lower_row = len(nums)
    left_col = 0
    right_col = len(nums[0])
    new_arr = []

    while up_row < lower_row and left_col < right_col:

        if up_row == lower_row-1:
            for i in range(left_col, right_col):
                new_arr.append(nums[up_row][i])
            return new_arr

        if left_col == right_col-1:
            for i in range(up_row, lower_row):
                new_arr.append(nums[i][right_col-1])
            return new_arr

        for i in range(left_col, right_col):
            # print(nums[up_row][i])
            new_arr.append(nums[up_row][i])

        up_row += 1


        for i in range(up_row,  lower_row):
            # print(nums[i][right_col-1])
            new_arr.append(nums[i][right_col-1])
        right_col -= 1


        for i in range(right_col-1, left_col-1, -1):
            # print(nums[lower_row-1][i])
            new_arr.append(nums[lower_row-1][i])
        lower_row -= 1


        for i in range(lower_row-1, up_row-1, -1):
            # print(nums[i][left_col])

            new_arr.append(nums[i][left_col])
        left_col += 1

    return new_arr


nums= [[98,30,17],[38,96,90],[17,0,50],[44,12,67],[12,79,43],[43,63,40],[19,93,48]]
print(array_print(nums))

# 98 30 17
# 38 96 90
# 17 0 50
# 44 12 67
# 12 79 43
# 43 63 40
# 19 93 48


