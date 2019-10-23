#1.反转二叉树

#定义一个树的结点

class Node:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

    def inverttree(self, treenode):
        if treenode == None:
            return None
        temp = treenode.lchild
        treenode.lchild = treenode.rchild
        treenode.rchild = temp
        self.inverttree(treenode.lchild)
        self.inverttree(treenode.rchild)

#2. 求二叉树的深度
    def find_depth(self, treenode):
        if treenode== None:
            return 0
        ldepth = self.find_depth(self, treenode.lchild)
        rdepth = self.find_depth(self, treenode.rchild)

        return (max(ldepth, rdepth)+1)

#求二叉树深度 非递归(广度优先，层次遍历的做法)

    def find_depth(self, treenode):
        if not treenode:
            depth = 0
        q = []
        depth = 0
        q.append(treenode)
        while q:
            depth += 1
            l = len(q)
            while l!=0:
                node = q.pop(0)
                if node.lchild:
                    q.append(node.lchild)
                if node.rchild:
                    q.append(node.rchild)
                l -= 1

        return depth

# pre-order
def pre_order(root):
    if root == None:
        return
    L = []
    node = root
    L.append(root)

    while L:
        while node:
            print(node.data)
            node = node.lchild
            L.append(node)

        node = L.pop()
        node = node.rchild

# def pre_order(root):
#     if not root:
#         return
#     print(root.data)
#     pre_order(root.lchild)
#     pre_order(root.rchild)


# inorder
def in_order(root):
    if root == None:
        return

    L = []
    node = root
    L.append(root)

    while L:
        while node:
            node = node.lchild
            L.append(node)

        node = L.pop()
        print(node.data)
        node = node.rchild


# latter_order
def la_order(root):
    if root == None:
        return

    L1 = []
    L2 = []
    node = root
    L1.append(node)


    while L1:
        node = L1.pop()
        if node.lchild:
            L1.append(node.lchild)
        if node.rchild:
            L1.append(node.rchild)

        L2.append(node)

    while L2:
        n = L2.pop()
        print(n.data)

# 层次遍历
def levelorder(root):
    if root == None:
        return

    L = []
    node = root
    L.append(node)

    while L:
        node = L.pop(0)

        print(node.data)

        if node.lchild:
            L.append(node.lchild)
        if node.rchild:
            L.append(node.rchild)


# 求二叉树的直径
def BTtreelongpath(root):
    m = 0

    def dfs(root):
        if not root:
            return 0

        left = dfs(root.lchild)
        right = dfs(root.rchild)

        m = max(m, left+right)

        return max(left, right) + 1

    dfs(root)
    return m

# 二叉搜索树转双向链表
class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    def Convert(self, pRootOfTree):
        if pRootOfTree==None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead==None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead

# 生成由[1 : n]这n个数组成的所有二叉搜索树的个数
# 以i为根结点，f(i)为i是根结点时树的个数，设dp[n]为所求的解，dp[n]=f(1)+f(2)+..+f(n)
# f(i) = dp[i-1]*dp[n-i] 即 dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2]+..+dp[n-1]*dp[0]

def num_btree(n):
    dp = [0 for i in range(n+1)]
    dp[0], dp[1] = 1,1
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1]*dp[i-j]


    return dp[n]

# print(num_btree(3))

# 给前序遍历and中序遍历输出树
def constrbtree1(pre_or, in_or):
    if pre == []:
        return None
    root = Node(pre_or[0])
    root_id = in_or.index(pre_or[0])
    root.lchild = constrbtree1(pre_or[1:root_id+1], in_or[:root_id])
    root.rchild = constrbtree1(pre_or[root_id+1:], in_or[root_id+1:])

    return root

# 给后序遍历and中序遍历输出树
def constrbtree2(post_or, in_or):

    if not post_or:
        return

    root = Node(post_or[-1])
    rootid = in_or.index(post_or[-1])
    root.lchild = constrbtree2(post_or[:root_id], in_or[:root_id])
    root.rchild = constrbtree2(post_or[root_id:-1], in_or[root_id+1:])

    return root

