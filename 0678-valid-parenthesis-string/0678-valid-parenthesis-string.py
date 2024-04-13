class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        wildcard_stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == '*':
                wildcard_stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif wildcard_stack:
                    wildcard_stack.pop()
                else:
                    return False

        while stack and wildcard_stack:
            if stack[-1] > wildcard_stack[-1]:
                return False
            stack.pop()
            wildcard_stack.pop()

        return not stack
