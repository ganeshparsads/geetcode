import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = float("inf")

        while left <= right:

            mid = (right + left) // 2
            hours = self.get_hours(mid, piles)

            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result

    def get_hours(self, k, piles):
        # k is our eating speed
        result = 0
        for pile in piles:
            result += math.ceil(pile / k)
        return result
