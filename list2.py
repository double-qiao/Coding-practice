# 反转链表
class linkedlist:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverselist(phead):
    if not phead or not phead.next:
        return phead

    last = None
    while phead:
        temp = phead.next
        phead.next = last
        last = phead
        phead = temp

    return last


# 找到链表中倒数第k个数

def findkthtotail(k, phead):
    if not k or not phead:
        return None
    left, right = phead, phead

    for i in range(k-1)
        if not right.next
            return None
        right = right.next

    while right.next:
        right = right.next
        left = left.next

    return left
