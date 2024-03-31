class Solution:
    def equalFrequency(self, word: str) -> bool:
        ch = [0]*26
        
        for c in word:
            ch[ord(c) - 97] += 1
        
        ch.sort()
        
        idx = 0
        while ch[idx] == 0:
            idx += 1
        
        ch = ch[idx:]

        # import pdb
        # pdb.set_trace()

        ch[0] -= 1

        if ch[0] == 0:
            new_ch = ch[1:]
        else:
            new_ch = ch

        if len(set(list(new_ch))) == 1:
            return True

        ch[0] += 1

        ch[len(ch) - 1] -= 1

        if len(set(list(ch))) == 1:
            return True      
        
        return False