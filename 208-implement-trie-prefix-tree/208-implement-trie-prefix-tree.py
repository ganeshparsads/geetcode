class Trie:
    
    class TrieNode:
        def __init__(self):
            self.word = False
            self.children = {}

    def __init__(self):
        self.node = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.node
        for i in range(len(word)):



            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                node.children[word[i]] = self.TrieNode()

                node = node.children[word[i]]

        if node.word==False:
            node.word = True

    def search(self, word: str) -> bool:
        node = self.node
        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                return False
        if node.word==True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:

        node = self.node
        for i in range(len(prefix)):
            if prefix[i] in node.children:
                node = node.children[prefix[i]]
            else:
                return False

        return True

        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)