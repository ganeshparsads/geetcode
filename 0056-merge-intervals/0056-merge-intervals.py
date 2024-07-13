class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort(key=lambda x: x[0])
        
        for each in intervals:
            if not stack:
                stack.append(each)
            elif stack[-1][1] < each[0]:
                stack.append(each)
            else:
                if stack[-1][1] >= each[1]:
                    continue
                else:
                    stack[-1][1] = each[1]
        
        return stack