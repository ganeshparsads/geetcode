from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        validate_map = {'}': '{', ')': '(', ']': '['}

        for i in s:
            if i not in validate_map:
                stack.append(i)
            else:
                if stack and stack[-1] == validate_map[i]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False

        return True

            