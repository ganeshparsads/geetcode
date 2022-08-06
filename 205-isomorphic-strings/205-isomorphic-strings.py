class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char not in freq_s:
                freq_s[s_char] = t_char
            else:
                if freq_s[s_char] != t_char:
                    return False
            if t_char not in freq_t:
                freq_t[t_char] = s_char
            else:
                if freq_t[t_char] != s_char:
                    return False
        return True
