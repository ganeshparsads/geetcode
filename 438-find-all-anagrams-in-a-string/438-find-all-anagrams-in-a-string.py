class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        end = 0
        
        freqMap = {}
        answers_list = []

        # build frequency map
        for char in p:
            if char not in freqMap:
                freqMap[char] = 0
            freqMap[char] += 1


        count = len(freqMap)
        strLen = len(s)
        windowLen = len(p)

        while end < strLen:

            endChar = s[end]

            # calculation
            if endChar in freqMap:
                freqMap[endChar] -= 1

                if freqMap[endChar] == 0:
                    count -= 1

            # check window
            if (end - start + 1) != windowLen:
                end += 1
            else:

                # fetch the answer
                if count == 0:
                    answers_list.append(start)

                startChar = s[start]
                if startChar in freqMap:
                    freqMap[startChar] += 1

                    if freqMap[startChar] == 1:
                        count += 1

                # slide the window
                start += 1
                end += 1

        return answers_list
        