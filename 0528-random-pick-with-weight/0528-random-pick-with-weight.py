class Solution:

    def __init__(self, w: List[int]):
        self.new_w = []
        
        self.total = 0
        for e in w:
            self.total += e
            self.new_w.append(self.total)

    def pickIndex(self) -> int:
        num = random.randint(1, self.total)
        
        for idx, val in enumerate(self.new_w):
            if num <= val:
                return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()