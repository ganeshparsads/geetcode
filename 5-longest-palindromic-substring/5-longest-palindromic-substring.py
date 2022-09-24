class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxy = ""
        n = len(s)
        for i in range(n):
            res = ""
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if left != right:
                    res = s[left] + res + s[right]
                else:
                    res = s[i]

                left -= 1
                right += 1
            
            if len(maxy) < len(res):
                maxy = res

        for i in range(n):
            res = ""
            left = i
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                if left != right:
                    res = s[left] + res + s[right]
                else:
                    res = s[i]

                left -= 1
                right += 1
            
            if len(maxy) < len(res):
                maxy = res

        return maxy