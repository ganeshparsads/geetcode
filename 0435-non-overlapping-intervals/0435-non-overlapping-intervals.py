class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        lastInterval = []
        intervals.sort(key=lambda x: x[1])
        
        for rec in intervals:
            if not lastInterval:
                lastInterval.append(rec)
            else:
                if lastInterval[-1][1] > rec[0]:
                    continue
                else:
                    lastInterval.append(rec)
        
        return len(intervals) - len(lastInterval)