class Solution:
    def __init__(self):
        self.result = []
    
    def palindrome_check(self, string):
        start = 0
        end = len(string) -1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        self.helper(s, 0, [])
        return self.result
    
    def helper(self, s, index, path):
        n = len(s)
        # base
        if index >= n:
            print(path)
            self.result.append(list(path))
            return
        
        # logic
        for i in range(index, n):
            subString = s[index:i+1]
            
            if self.palindrome_check(subString):
                # action
                path.append(subString)

                # recurse
                self.helper(s, i+1, path)
                
                # backtrack
                path.pop()
