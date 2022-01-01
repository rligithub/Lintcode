
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution: # DFS
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        if not root:
            return
        self.head, self.tail = None, None
        self.dfs(root)
        # circled linked list
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head

    def dfs(self,root):
        if not root:
            return
        # left
        self.dfs(root.left)
        # root
        if self.tail:
            self.tail.right = root
            root.left = self.tail
        else:
            self.head = root
        self.tail = root
        # right
        self.dfs(root.right)


class Solution2:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        # Write your code here.
        if root is None:
            return None

        start, end = self.dfs(root)
        end.right = start
        start.left = end
        return start

    def dfs(self, root):
        if not root:
            return None, None
        left_start, left_end = self.dfs(root.left)
        right_start, right_end = self.dfs(root.right)

        #  left <> root
        if left_end:
            left_end.right = root
            root.left = left_end

        # right <> root
        if right_start:
            root.right = right_start
            right_start.left = root

        start = left_start or root or right_end
        end = right_end or root or left_start

        return start, end