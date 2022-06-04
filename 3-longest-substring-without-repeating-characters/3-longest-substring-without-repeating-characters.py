class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0

        maxLen = 0
        seen = deque()
        strList = list(s)
        strLen = len(s)

        for end in range(strLen):
            if strList[end] not in seen:
                seen.append(strList[end])
            else:
                maxLen = max(maxLen, len(seen))
                ele = ''
                while seen and ele != strList[end]:
                    start += 1
                    ele = seen.popleft()

                seen.append(strList[end])

        maxLen = max(maxLen, len(seen))
        return maxLen