# 判断链表是否有环 (快慢指针)
class LNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def exitLoop(phead):
    p1 = p2 = phead
    while p2 and p2.next:  # 当链表为空或者只有一个结点时，就不执行循环体里的程序，返回False
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False


if __name__ == "__main__":
    LList = LNode(1)
    p1 = LNode(2)
    p2 = LNode(3)
    p3 = LNode(4)
    p4 = LNode(5)
    p5 = LNode(6)
    LList.pnext = p1
    p1.pnext = p2
    p2.pnext = p3
    p3.pnext = p4
    p4.pnext = p5
    p5.pnext = p2
    print(exitLoop(LList))

# 求两个链表的第一个公共结点
# 让长度短的链表达到终点后指向长度长的链表的头结点

def findcommonnode(phead1, phead2):
    p1, p2 = phead1, phead2

    while p1 != p2:
        if p1:
            p1=p1.next
        else:
            p1 = phead2

        if p2:
            p2 = p2.next
        else:
            p2 = phead1


    return p1

# 合并两个有序的链表
# 需要两个指针分别指向两个链表的头节点

def mergelist(phead1, phead2):
    if not phead1:
        return phead2
    if not phead2:
        return phead1

    cur1, cur2 = phead1, phead2
    phead = LNode(0)
    new_list = phead

    while cur1 != None and cur2 != None:

        if cur1.val <= cur2.val:
            phead.next = cur1
            cur1 = cur1.next

        if cur1.val == cur2.val:
            cur2 = cur2.next

        else:
            phead.next = cur2
            cur2 = cur2.next

        phead = phead.next

    if cur1 != None:
        phead.next = cur1

    if cur != None:
        phead.next = cur2

    return new_list.next

#
