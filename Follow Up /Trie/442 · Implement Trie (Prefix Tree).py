class TrieNode:
    # TrieNode的两个功能：.next 和 .isWord
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def find(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node:
                return None
        return node

    def search(self, word):
        node = self.find(word)
        return node is not None and node.isWord

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        return self.find(prefix) is not None

