from collections import Counter

class Solution:
    def reorganizeString(self, s):
        freq_dict = [0]*26
        
        letter_cnter = Counter(s)
        
        for key, val in letter_cnter.items():
            asci = ord(key)
            diff = asci - 97
            freq_dict[diff] = val

        max_val = 1
        prev_idx = -1
        res = []

        while max_val > 0:
            max_val = -1
            selected_idx = prev_idx
            for idx, val in enumerate(freq_dict):
                if max_val <= val and selected_idx != idx:
                    max_val = val
                    selected_idx = idx

            if max_val > 0 and prev_idx != selected_idx:
                prev_idx = selected_idx
                extract_char = chr(selected_idx + 97)
                res.append(extract_char)
                freq_dict[selected_idx] -= 1
                print(max_val, freq_dict)

        print(freq_dict)

        res = ''.join(res)

        print(res)

        if len(res) != len(s):
            return ""

        return res



obj = Solution()
print("Result: ", obj.reorganizeString("vvvlo"))
