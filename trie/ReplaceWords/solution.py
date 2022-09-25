from collections import deque

class TrieNode:
    def __init__(self):
        self.char = ["" for i in range(26)]
        self.wordEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        curr = self.root

        for i in word:
            if not curr.char[ord(i) - 97]:
                curr.char[ord(i) - 97] = TrieNode()
            curr = curr.char[ord(i) - 97]

        curr.wordEnd = True

    def search(self, word):
        curr = self.root

        for i in word:
            if not curr.char[ord(i) - 97]:
                return False
            curr = curr.char[ord(i) - 97]

        return curr.wordEnd


    def runBfs(self, curr, prefix):
        result = []
        bfsStack = deque()
        bfsStack.append((curr, prefix))

        while bfsStack:
            size = len(bfsStack)

            for i in range(size):
                curr, prefix = bfsStack.popleft()
                if curr.wordEnd:
                    result.append(prefix)
                for j in range(26):
                    if curr.char[j]:
                        new_prefix = prefix + chr(j+97)
                        bfsStack.append((curr.char[j], new_prefix))

        return result

    # modify prefix
    def startsWith(self, word):
        curr = self.root

        prefix = ''

        for i in word:
            if not curr.char[ord(i) - 97]:
                return {}
            curr = curr.char[ord(i) - 97]

        group = self.runBfs(curr, word)

        result = {}

        for compl in group:
            result[compl] = word

        return result

class Solution:

    def __init__(self):
        pass

    def replaceWords(self, dictionary, sentence):
        obj = Trie()

        for word in sentence.split(' '):
            obj.insert(word)

        for word in sentence.split(' '):
            print(word, obj.search(word))

        result = {}

        for word in dictionary:
            result.update(obj.startsWith(word))

        final_sentence = []
        for word in sentence.split(' '):
            if word in result:
                final_sentence.append(result[word])
            else:
                final_sentence.append(word)

        return ' '.join(final_sentence)


dictionary = [
    "cat",
    "mat",
    "rat"
]

sentence = "The their cattle"

obj = Solution()

print(obj.replaceWords(dictionary, sentence))