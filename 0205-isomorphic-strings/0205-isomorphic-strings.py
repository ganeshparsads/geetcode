class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_dict = {}
        visited_set = set()
        
        n = len(s)
        
        if n != len(t):
            return False
        
        for i in range(n):
            src = s[i]
            term = t[i]
            if src not in letter_dict:
                if term in visited_set:
                    return False
                
                letter_dict[src] = term
                visited_set.add(term)
            
            if src in letter_dict:
                if letter_dict[src] != term:
                    return False
            
        
        return True
                