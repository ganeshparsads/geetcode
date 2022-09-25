from collections import defaultdict

class Solution:
    def longestPalindrome(self, words):
        # import pdb
        # pdb.set_trace()
        duplicate_counter = 0
        count = 0
        hMap = defaultdict(int)

        for word in words:
            if word[1] == word[0]:
                duplicate_counter += 1

            if word[::-1] not in hMap:
                hMap[word] += 1
            else:
                hMap[word[::-1]] -= 1
                if not hMap[word[::-1]]:
                    hMap.pop(word, None)
                count += 4
                if word == word[::-1]:
                    duplicate_counter -= 2

        if duplicate_counter:
            count += 2

        return count
            
obj = Solution()
words = ["mm","mm","yb","by","bb","bm","ym","mb","yb","by","mb","mb","bb","yb","by","bb","yb","my","mb","ym"]
print(obj.longestPalindrome(words))
