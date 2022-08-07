from math import ceil

class Solution:
    # return hash value
#     def hashFunc(self, phrase, n):
#         hashVal = 10000
#         for l in phrase:
#             hashVal -= ord(l)

#         return hashVal
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        n = len(strs)
        for word in strs:
            # hashVal = self.hashFunc(word, n)
            hashVal = "".join(sorted(word))
            
            if hashVal not in hashMap:
                hashMap[hashVal] = []
            hashMap[hashVal].append(word)

        return hashMap.values()
        