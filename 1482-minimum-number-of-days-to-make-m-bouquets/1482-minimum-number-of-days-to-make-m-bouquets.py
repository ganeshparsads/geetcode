class Solution:
    def possible(self, bloomDay, day, m, k):
        cnt = 0
        nob = 0
        
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                cnt += 1
            else:
                nob += (cnt // k)
                cnt = 0
        
        nob += (cnt // k)
        
        if nob >= m:
            return True
        
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        low = min(bloomDay)
        high = max(bloomDay)
        
        res = -1
        
        while low <= high:
            mid = low + (high-low)//2
            
            if self.possible(bloomDay, mid, m, k):
                res = mid
                high = mid - 1
            
            else:
                low = mid + 1
        return res
        