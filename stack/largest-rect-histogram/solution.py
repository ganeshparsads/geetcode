class Solution:
    """
    prob: 496 => https://leetcode.com/submissions/detail/700250704/
    """
    def nearesetLowestRight(self, ip):
        stack = []
        span = []

        size = len(ip)

        for idx, num in enumerate(reversed(ip)):
            if not stack:
                stack.append([num, idx])
                span.append(idx + 1)
                continue

            if stack[-1][0] < num:
                span.append(idx - stack[-1][1])
                stack.append([num, idx])
            else:
                while stack and stack[-1][0] >= num:
                    stack.pop()

                if not stack:
                    span.append(idx + 1)
                else:
                    span.append(idx - stack[-1][1])

                stack.append([num, idx])

        return list(reversed(span))
    
    def nearesetLowestLeft(self, ip):
        stack = []
        span = []

        for idx, num in enumerate(ip):
            if not stack:
                stack.append([num, idx])
                span.append(idx + 1)
                continue

            if stack[-1][0] < num:
                span.append(idx - stack[-1][1])
                stack.append([num, idx])
            else:
                while stack and stack[-1][0] >= num:
                    stack.pop()

                if not stack:
                    span.append(idx + 1)
                else:
                    span.append(idx - stack[-1][1])

                stack.append([num, idx])

        return span
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = self.nearesetLowestLeft(heights)
        right = self.nearesetLowestRight(heights)

        maxy = 0

        for idx, num in enumerate(heights):
            width = left[idx] + right[idx] - 1
            maxy = max(maxy, width * num)

        return maxy
