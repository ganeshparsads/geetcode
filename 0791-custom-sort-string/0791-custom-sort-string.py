class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_map = dict(Counter(s))
        
        result = []
        
        for letter in order:
            if letter in hash_map:
                result.append(letter*hash_map[letter])
                
                hash_map.pop(letter)
        
        for key, val in hash_map.items():
            result.append(key*val)
        
        return "".join(result)