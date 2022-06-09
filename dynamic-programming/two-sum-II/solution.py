class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            if (target - num) in numbers[idx:]:
                return (idx+1), (numbers[idx:].index(target - num) + 1)
