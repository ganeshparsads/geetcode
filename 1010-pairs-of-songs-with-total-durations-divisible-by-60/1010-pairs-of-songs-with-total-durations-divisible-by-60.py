class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #the songs whose time % 60 != 0, get its time % 60
        odd = [i % 60 for i in time if i % 60]
        #the amount of songs whoes time % 60 == 0
        good = len(time) - len(odd)
        rst = good * (good - 1) // 2
        ct = collections.Counter(odd)
        for k in ct:
            if k == 30: rst += ct[30] * (ct[30] - 1) // 2
            else: rst += ct[k] * ct[60-k]
            #avoid repeat count
            ct[k] = 0
        return rst