from collections import deque

class Solution:
    validate_map = {'}': '{', ')': '(', ']': '['}
    def isValid(self, s):
        # with O(n) space
        # stack = deque()

        # for i in s:   
        #     if i not in validate_map:
        #         stack.append(i)
        #     else:
        #         if stack and stack[-1] == validate_map[i]:
        #             stack.pop()
        #         else:
        #             return False
        # if stack:
        #     return False

        # return True

        # with O(1) space
        top = -1

        for idx, i in enumerate(s):
            if i in self.validate_map:
                top = idx
            else:
                if top == -1 or self.validate_map[i] != s[top]:
                    return False
                else:
                    top = self.getTop(s, top-1)

        return top == -1

    def getTop(self, s, idx):
        right = 0

        while idx >= 0:
            ch = s[idx]

            if ch in self.validate_map:
                right += 1
            else:
                right -= 1

            if right < 0:
                return idx

            idx -= 1

        return -1

obj = Solution()

print(obj.isValid('{}'))