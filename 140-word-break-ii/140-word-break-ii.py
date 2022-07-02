class Solution:
    def dfs(self, s, wordDict, start, res, curr_sentence):
        if start == len(s):
            res.append(' '.join(curr_sentence[:]))
            return
        
        for end in range(start + 1, len(s) + 1):
            if s[start: end] in wordDict:
                curr_sentence.append(s[start: end])
                self.dfs(s, wordDict, end, res, curr_sentence)
                curr_sentence.pop()
                
                
            
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        self.dfs(s, wordDict, 0, res, [])
        return res