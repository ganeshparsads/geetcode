class Solution:
    def __init__(self):
        self.result = 0
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        self.backtrack(n, "0")
        return self.result
    
    def backtrack(self, n, path):
        if n == 0:
            self.result += 1
            return

        str_num = [str(i) for i in range(10)]

        for num in str_num:
            # try to get rid of leading zero
            nlz_path = str(int(path))
            if num not in nlz_path or nlz_path=="0":
                self.backtrack(n-1, nlz_path+num)