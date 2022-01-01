class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        if not words or not words[0]:
            return []
        self.res = []
        self.trie = Trie()
        self.visited = set()
        self.find = set()

        for word in words:
            self.trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                self.visited.add((i, j))
                self.dfs(board, i, j, self.trie.root.children.get(char))
                self.visited.remove((i, j))
        return self.res

    def dfs(self, board, x, y, node):
        if not node:
            return
        if node.isWord and node.path not in self.find:
            self.res.append(node.path)
            self.find.add(node.path)

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            xx, yy = x + dx, y + dy
            if 0 <= xx < len(board) and 0 <= yy < len(board[0]) and (xx, yy) not in self.visited:
                newChar = board[xx][yy]
                self.visited.add((xx, yy))
                self.dfs(board, xx, yy, node.children.get(newChar))
                self.visited.remove((xx, yy))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.path = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True
        node.path = word

    def find(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children.get(char)
        return node.isWord




board = ["doaf","agai","dcan"]
words = ["dog","dad","dgdg","can","again"]

a = Solution()
print(a.wordSearchII(board,words))