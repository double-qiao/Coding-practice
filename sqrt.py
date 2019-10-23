#计算一个正整数的平方根

def mysqrt(num):
    if num<=0:
        return None
    low = 0.0
    high = num*1.0

    while low <= high:
        mid = (low + high) / 2
        if  abs(num - mid**2) < 0.000001:
            return mid
        elif mid**2<num:
            low = mid
        else:
            high = mid

    # return high

print(mysqrt(18))