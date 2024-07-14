class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []

        minVal = 100000
        maxVal = -1
        
        for rec in intervals:
            if rec[0] > newInterval[1] or rec[1] < newInterval[0]:
                stack.append(rec)
            else:
                minVal = min(minVal, rec[0], newInterval[0])
                maxVal = max(maxVal, rec[1], newInterval[1])
                # print(rec, minVal)
        
        if minVal != 100000:
            stack.append([minVal, maxVal])
        else:
            stack.append(newInterval)
        
        stack.sort(key=lambda x: x[0])
        
        return stack
                
                    