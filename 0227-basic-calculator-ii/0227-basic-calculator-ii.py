class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        s.strip()
        curr_num = 0
        last_sign = "+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num*10 + int(s[i])
            if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
                if last_sign == "+":
                    stack.append(curr_num)
                elif last_sign == "-":
                    stack.append(-1*curr_num)
                elif last_sign == "*":
                    stack.append(curr_num * stack.pop())
                elif last_sign == "/":
                    stack.append(int(stack.pop() / curr_num))
                last_sign = s[i]
                curr_num = 0
            
        result = 0

        while stack:
            result += stack.pop()
        
        return result
                