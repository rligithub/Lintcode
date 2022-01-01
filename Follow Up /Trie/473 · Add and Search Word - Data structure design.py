class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in noxde.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def search(self, word):
        if word is None:
            return False

        return self.searchHelper(word, self.root, 0)

    def searchHelper(self, word, root, start_index):
        for i in range(start_index, len(word)):
            if word[i] == ".":
                for node in root.children:
                    if self.searchHelper(word, root.children[node], i + 1):
                        return True
                else:
                    return False

            if word[i] in root.children:
                root = root.children[word[i]]
            else:
                return False

        return root.isWord


a = WordDictionary()
a.addWord("bad")
a.addWord("dad")
a.addWord("mad")
print(a.search("pad"))
print(a.search("bad"))
print(a.search(".ad"))
print(a.search("b.."))





