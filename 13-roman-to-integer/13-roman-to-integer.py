class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_let_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = list(s)
        
        last_max = ""
        
        dig = 0
        
        for i in range(len(s) - 1, -1, -1):
            if not last_max or roman_to_let_dict[last_max] < roman_to_let_dict[s[i]]:
                last_max = s[i]
            if last_max != s[i]:
                dig = dig - roman_to_let_dict[s[i]]
            else:
                dig = dig + roman_to_let_dict[s[i]]
        
        return dig
