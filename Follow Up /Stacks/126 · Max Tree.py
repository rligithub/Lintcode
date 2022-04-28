
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # for each num, create a node
    # descending --> save node into stack
    # ascending --> pop node from stack --> (known: node < curnode and prenode < node) compare prenode and curnode
    # connect node with smaller of prenode or curnode
    # append node with children to stack

    # NOTE: need to add [float('inf'] in array to avoid that --> if last value in array is smaller than stack[-1], last node won't connect any nodes
    # NOTE: return stack[-1].left
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """

    def maxTree(self, A):
        if not A:
            return
        # stack里面存的是node，保存降序node，升序则pop
        # 已知： 倒二 > 倒一， 倒一 < cur ； 比较倒二和cur，较小者作为 倒一 的子孩子
        stack = []
        # 在array末尾加一个无限值，为了防止 最后一位是 比stack里的数小，然后append到stack，还没跟其他node连起来
        for num in (A + [float('inf')]):
            cur = TreeNode(num)
            while stack and cur.val > stack[-1].val:
                pre = stack.pop()
                if stack and cur.val > stack[-1].val:
                    stack[-1].right = pre
                else:
                    cur.left = pre

            stack.append(cur)
        return stack[-1].left  # 倒一就是root 就是 ['inf']


A = [2, 5, 6, 0, 3, 1]
a = Solution()
print(a.maxTree(A).val)