
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution1: # DFS
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """

    def maxTree(self, A):
        if not A:
            return None

        mid = A.index(max(A))
        node = TreeNode(A[mid])

        node.left = self.maxTree(A[:mid])
        node.right =self.maxTree(A[mid+1:])
        return node

class Solution2:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """

    def maxTree(self, A):
        if not A:
            return None

        stack = []

        for index, num in enumerate(A):
            cur = TreeNode(num)
            while stack and stack[-1].val < cur.val:
                pre = stack.pop()
                if stack and stack[-1].val < cur.val:
                    stack[-1].right = pre
                else:
                    cur.left = pre
            stack.append(cur)
        return stack[-1].left



A = [2, 5, 6, 0, 3, 1]
a = Solution2()
print(a.maxTree(A))