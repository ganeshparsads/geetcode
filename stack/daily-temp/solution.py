# import deque

class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0 for i in range(len(temperatures))]
        n = len(result)
        last_idx = -1
        stack = []
        result = []
        for i in range(n-1, -1, -1):
            if not stack:
                stack.append((temperatures[i], i))
                result.append(0)

            else:
                while stack and stack[-1][0] < temperatures[i]:
                    stack.pop()
                
                if stack:
                    result.append(stack[-1][1] - i)
                else:
                    result.append(0)
                print("here: ", i)
                stack.append((temperatures[i], i))
        result.reverse()

        return result

obj = Solution()

print(obj.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
