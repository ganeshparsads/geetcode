class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort(key=lambda x: x[0])
        
        for i in intervals:
            if not stack:
                stack.append(i)
            else:
                if stack[-1][1] >= i[0]:
                    if i[1] > stack[-1][1]:
                        stack[-1][1] = i[1]
                else:
                    stack.append(i)
        
        return stack