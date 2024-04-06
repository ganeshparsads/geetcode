class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for i in s:
            if not stack:
                stack.append(i)
            else:
                
                if (ord(stack[-1]) >= 97 and stack[-1].upper() == i) or ( 65<=ord(stack[-1])< 97 and stack[-1].lower() == i):
                    stack.pop()
                else:
                    stack.append(i)
        
        return ''.join(stack)
                