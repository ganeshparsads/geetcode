class Solution:
    def getMaxLen(self, nums):
        prevMaxtuple = tuple()
        prevMintuple = tuple()
        
        res = 0

        for n in nums:
            currMaxTuple = tuple()
            currMinTuple = tuple()
            if n == 0:
                currMinTuple = (1, 0)
                currMaxTuple = (1, 0)
            elif not prevMaxtuple and not prevMintuple:
                currMinTuple = (n, 1)
                currMaxTuple = (n, 1)
            else:
                # (tempMaxVal, tempMaxCnt) = maxStack[-1]

                # select the max from minStack or maxStack
                if  prevMintuple[0]*n < 0 and prevMaxtuple[0]*n < 0:
                    currMaxTuple = (n, 1)
                elif prevMintuple[0]*n == prevMaxtuple[0]*n:
                    currMaxTuple = (prevMintuple[0]*n, max(prevMintuple[1], prevMaxtuple[1]) + 1)
                elif prevMintuple[0]*n > prevMaxtuple[0]*n:
                    currMaxTuple = (prevMintuple[0]*n, prevMintuple[1]+1)
                else:
                    currMaxTuple = (prevMaxtuple[0]*n, prevMaxtuple[1]+1)
                
                # select the min from minStack or maxStack
                if  prevMintuple[0]*n > 0 and prevMaxtuple[0]*n > 0:
                    currMinTuple = (n, 1)
                elif prevMintuple[0]*n == prevMaxtuple[0]*n:
                    currMinTuple = (prevMintuple[0]*n, max(prevMintuple[1], prevMaxtuple[1]) + 1)
                elif prevMintuple[0]*n < prevMaxtuple[0]*n:
                    currMinTuple = (prevMintuple[0]*n, prevMintuple[1]+1)
                else:
                    currMinTuple = (prevMaxtuple[0]*n, prevMaxtuple[1]+1)

            prevMaxtuple = currMaxTuple
            prevMintuple = currMinTuple
            if prevMaxtuple[0] > 0:
                res = max(prevMaxtuple[1], res)

        return res

arr = [0, 1,-2,-3, -4]
obj = Solution()
print(obj.getMaxLen(arr))