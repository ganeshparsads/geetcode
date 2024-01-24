class Solution:
    def decodeString(self, s: str) -> str:
        chr_stack = []
        num_stack = []
        curr_str = ""
        curr_num = 0

        for i in range(len(s)):
            if s[i] == "]":
                num = num_stack.pop()
                curr_str = curr_str*num
                curr_str = chr_stack.pop() + curr_str
            elif s[i] == "[":
                chr_stack.append(curr_str)
                num_stack.append(curr_num)                
                curr_str = ""
                curr_num = 0
            else:
                if s[i].isalpha():
                    curr_str += s[i]
                else:
                    curr_num = curr_num*10 + int(s[i])

        return curr_str
