from collections import defaultdict, Counter

class Solution:
    def longestPalindrome(self, words):
        count = Counter(words)
        hMap = defaultdict(int)
        res = 0
        hasOdd = False
        for word, freq in count.items():
            # same letters
            if word[::-1] == word:
                # odd
                if freq % 2 != 0:
                    hasOdd = True
                    res += (freq-1)*2
                else:
                    res += freq*2
            else:
                if count[word] > 0 and word[::-1] in count and count[word[::-1]] > 0:
                    c = min(count[word[::-1]], count[word])
                    res += c*4
                    count[word] -= c
                    count[word[::-1]] -= c
        
        if hasOdd:
            res += 2
        return res