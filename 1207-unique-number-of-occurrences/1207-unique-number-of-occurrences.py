class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = list(dict(Counter(arr)).values())
        if len(freq) != len(set(freq)):
            return False

        return True
    