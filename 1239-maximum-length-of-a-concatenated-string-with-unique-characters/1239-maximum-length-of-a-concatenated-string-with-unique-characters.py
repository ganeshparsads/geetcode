class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, current_string):
            unique_length = len(set(current_string))
            if unique_length != len(current_string):
                return 0

            max_length = len(current_string)
            for i in range(index, len(arr)):
                max_length = max(max_length, backtrack(i + 1, current_string + arr[i]))
            
            return max_length

        return backtrack(0, "")