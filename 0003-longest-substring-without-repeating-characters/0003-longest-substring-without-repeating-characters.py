class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        i = 0
        j = 0
        
        hashSet = set()
        result = 0
        
        for let in s:
            if let in hashSet:
                result = max(len(hashSet), result)
                while True:
                    char = s[i]
                    hashSet.remove(char)
                    i += 1

                    if char == let:
                        break

            hashSet.add(let)
                
        
        result = max(len(hashSet), result)
        
        return result