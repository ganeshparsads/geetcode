class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        new_str = []
        
        for idx, i in enumerate(s):
            if i == '(' or i == ')':
                if i == ')' and stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((i, idx))
        indices = set()
        
        for i in stack:
            indices.add(i[1])
        
        for idx, letter in enumerate(s):
            if idx not in indices:
                new_str.append(letter)
        
        return ''.join(new_str)
        