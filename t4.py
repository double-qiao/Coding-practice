# 1. 字符串A转化为字符串B的最小编辑次数。允许的编辑操作有：删除，插入，替换。

def strAToB(str1, str2):
    l1 = len(str1) + 1
    l2 = len(str2) + 1

    # 初始化矩阵，行列长度比字符串长度各大1
    #     b e a u t y
    #   0 1 2 3 4 5 6
    # b 1
    # a 2
    # t 3
    # y 4
    # u 5

    matrix = [[0]*l1 for n in range(l2)]
    for i in range(l1):
        matrix[0][i] = i
    for j in range(l2):
        matrix[j][0] = j

    # 字符串下标从0开始，矩阵下标从1开始
    for i in range(1, l2):
        for j in range(1, l1):
            if str1[j-1] == str2[i-1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+cost)

    return matrix[l2-1][l1-1]


# 2. 求字符串的最长回文 "abbacefg"

# 首先需要填充原先的字符串，使其长度为奇数。遍历得到不同点的中心点的回文长度

def max_length(string):
    str = "#"+"#".join(string)+"#"
    l = len(str)
    m = 0
    for i in range(1, l):
        cur_length = get_length(str, i)
        m = max(m, cur_length)

    return m

def get_length(str, index):
    l = 0
    for i in range(1, index+1):
        if index+i<len(str) and str[index-i]==str[index+i]:
            l += 1
        else:
            break

    return l


# print(max_length('35534321'))


print(strAToB("book","block"))