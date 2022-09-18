from collections import Counter

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        if n == 1:
            return ''
        mid = n//2
        
        for i in range(mid):
            if palindrome[i] != "a":
                palindrome = list(palindrome)
                palindrome[i] = "a"
                palindrome = ''.join(palindrome)
                return palindrome

        palindrome = list(palindrome)
        palindrome[n - 1] = 'b'
        return ''.join(palindrome)
        