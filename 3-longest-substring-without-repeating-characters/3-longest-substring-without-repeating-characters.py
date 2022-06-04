class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0

        maxLen = 0
        windowString = deque()
        strList = list(s)
        strLen = len(s)

        while end < strLen:
            if strList[end] not in windowString:
                windowString.append(strList[end])
                end += 1

            else:
                maxLen = max(maxLen, len(windowString))
                ele = ''
                while windowString and ele != strList[end]:
                    start += 1
                    ele = windowString.popleft()

                windowString.append(strList[end])
                end += 1
        maxLen = max(maxLen, len(windowString))
        return maxLen