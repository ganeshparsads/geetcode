class Solution:
    def calculate(self, s: str) -> int:
        it = 0
        
        def calc():
            nonlocal it
            
            def update(op, v):
                if op == "+":
                    stack.append(v)
                elif op == "-":
                    stack.append(-v)
                elif op == "*":
                    stack.append(stack.pop() * v)
                else:
                    stack.append(stack.pop() / v)
            num = 0
            stack = []
            sign = "+"
            
            while it < len(s):
                if s[it].isdigit():
                    num = num*10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    it += 1
                    num = calc()
                elif s[it] == ")":
                    # last number update
                    update(sign, num)
                    return sum(stack)
                
                it += 1

            # last number update                
            update(sign, num)
            return sum(stack)

        return calc()