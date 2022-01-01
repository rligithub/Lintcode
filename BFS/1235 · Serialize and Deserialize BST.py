from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param data: a string after a tree serializing
    @return: the tree after a string deserialization
    """

    def deserialize(self, data: str) -> TreeNode:
        if len(data) == 0:
            return None

        node = data.split(',')
        root = TreeNode(int(node[0]))
        queue = collections.deque([root])
        idx = 1
        while queue:
            # left node
            if idx == len(node):
                break  # 处理完所有data，而队列不一定为空，需要停止
            cur = queue.popleft()
            if node[idx] != '#':
                cur.left = TreeNode(str(node[idx]))
                queue.append(cur.left)
            idx += 1

            # right node
            if idx == len(node):
                break  # 处理完所有data，而队列不一定为空，需要停止
            if node[idx] != '#':
                cur.right = TreeNode(str(node[idx]))
                queue.append(cur.right)
            idx += 1
        return root

    """
    @param treeNode: A tree that needs to be serialized
    @return: the string after a tree serializing
    """

    def serialize(self, treeNode: TreeNode) -> str:
        # BFS, mark None as #
        if not treeNode:
            return ''

        queue = collections.deque([treeNode])
        res = []
        while queue:
            cur = queue.popleft()
            if cur is None:
                res.append('#')
            else:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)

        n = len(res)  # 去掉最后的‘#’节省空间
        print(res)
        for i in range(n - 1, -1, -1):
            if res[i] == '#':
                res.pop()
            else:
                break
        print(res)
        return ','.join(res)
######################################################################

from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param data: a string after a tree serializing
    @return: the tree after a string deserialization
    """

    def deserialize(self, data: str) -> TreeNode:
        # write your code here
        items = data.split(" ")
        print(items)
        if not items:
            return None
        root = TreeNode(items[0])
        queue = collections.deque([root])
        index = 1

        while index < len(items):
            node = queue.popleft()
            # if index < len(items):
            if items[index] != "#":
                left_node = TreeNode(items[index])
                node.left = left_node
                queue.append(node.left)
            index += 1
            if items[index] != "#":
                right_node = TreeNode(items[index])
                node.right = right_node
                queue.append(node.right)
            index += 1
        return root

    """
    @param treeNode: A tree that needs to be serialized
    @return: the string after a tree serializing
    """

    def serialize(self, root: TreeNode) -> str:
        # write your code here
        if not root:
            return ""
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            result.append(str(node.val) if node else '#')

            if node:
                queue.append(node.left)
                queue.append(node.right)

        print(result)
        return " ".join(result)