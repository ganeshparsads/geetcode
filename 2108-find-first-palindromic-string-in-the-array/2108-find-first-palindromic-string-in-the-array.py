class Solution:
    def validatePalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s.lower())
        return s == s[::-1]
        
    
    def firstPalindrome(self, words: List[str]) -> str:
        for each in words:
            if self.validatePalindrome(each):
                return each
        return ""
