import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = dict(Counter(s))
        
        minHeap = []
        
        for key, val in cnt.items():
            heapq.heappush(minHeap, (-val, key))
        
        result = []
        
        prev_letter = "$"
        prev_freq = -10000

        # import pdb
        # pdb.set_trace()
        
        for i in range(len(s)):
            if not minHeap:
                break

            freq, letter = heapq.heappop(minHeap)

            if prev_freq >= 1:
                heapq.heappush(minHeap, (-prev_freq, prev_letter))

            result.append(letter)
            prev_letter = letter
            prev_freq = -freq - 1

        if len(result) == len(s):
            return "".join(result)
        
        return ""
