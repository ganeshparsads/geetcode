class Solution:

    def __init__(self, w: List[int]):
#         self.new_w = {}
        
#         self.total = 0
#         for idx, val in enumerate(w):
#             self.new_w[idx] = [self.total, self.total + val]
#             self.total += val
        self.intervals = {}
        self.num_parts = 0
        for i, w in enumerate(w):
            self.intervals[i] = [self.num_parts, self.num_parts + w]
            self.num_parts += w

    def pickIndex(self) -> int:
#         num = random.randint(1, self.total-1)
        
#         low = 0
#         high = len(self.new_w) - 1
        
#         print(self.new_w)
        
#         while True:
#             mid = low + (high - low)//2 
            
#             if self.new_w[mid][0] <= num < self.new_w[mid][1]:
#                 return mid
#             elif num < self.new_w[mid][0]:
#                 right = mid - 1
#             elif num >= self.new_w[mid][1]:
#                 left = mid + 1
        rand_val = random.randint(0, self.num_parts-1)

        left = 0
        right = len(self.intervals) - 1
        while True:
            mid = left + (right - left) // 2

            if self.intervals[mid][0] <= rand_val < self.intervals[mid][1]:
                return mid
            elif rand_val < self.intervals[mid][0]:
                right = mid - 1
            elif rand_val >= self.intervals[mid][1]:
                left = mid + 1



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()