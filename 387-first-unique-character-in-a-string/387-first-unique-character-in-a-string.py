class Solution:
    def firstUniqChar(self, s: str) -> int:
        array = [100000 for i in range(26)]

        s = list(s)
        for idx in range(len(s)-1, -1, -1):
            char_idx = ord(s[idx]) - 97
            if array[char_idx] == 100000:
                array[char_idx] = idx
            elif array[char_idx] != 10000 and array[char_idx] != 50000:
                array[char_idx] = 50000
        
        result = min(array)

        if result == 100000 or result == 50000:
            return -1

        return result
