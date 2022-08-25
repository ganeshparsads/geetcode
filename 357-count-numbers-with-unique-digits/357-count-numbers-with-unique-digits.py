import math

class Solution:
    def __init__(self):
        self.result = 0

    def getNDigitNumbers(self, n):
        return 10**n - 10**(n-1)
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # self.backtrack(n, "0")

        # (duplicate, non-duplicates)
        # number of numbers which are duplicate 
        dp = [(0, 0) for i in range(n+1)]

        # initialize DP
        # number of duplicates in zero is zero
        # number of duplicates in zero is 1
        dp[0] = (0, 1)

        for i in range(1, n+1):
            numberOfdigits = self.getNDigitNumbers(i)
            print(i)
            prev_dup, prev_non_dup = dp[i-1]
            duplicates = prev_dup*10 + (i-1) * prev_non_dup
            non_duplicates = numberOfdigits - duplicates
            dp[i] = (duplicates, non_duplicates)

        final_sum = 0
        for i in range(n+1):
            final_sum += dp[i][1]

        return final_sum
    
    def backtrack(self, n, path):
        if n == 0:
            self.result += 1
            return

        str_num = [str(i) for i in range(10)]

        for num in str_num:
            # try to get rid of leading zero
            new_path = str(int(path))
            if num not in new_path or new_path=="0":
                self.backtrack(n-1, nlz_path+num)
