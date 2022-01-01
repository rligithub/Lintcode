class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.wordtable = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node.wordtable.append(word)
            node = node.children[char]

    def find(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]



