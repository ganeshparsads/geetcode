class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        temp = set()

        for i in list(s):
            if i not in temp:
                temp.add(i)
            else:
                count += 1
                temp = set(i)

            
        return count+1

obj = Solution()

print(obj.partitionString('abacaba'))
