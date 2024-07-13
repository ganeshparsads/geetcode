class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        i = j = 0
        x = [[positions[i], healths[i], directions[i], i] for i in range(len(positions))]
        s = sorted(x, key=lambda x: x[0])
        ans = []
        stack = []
        while i < len(s):
            if s[i][2] == 'L' and len(stack) == 0:
                ans.append([s[i][1], s[i][3]])
                i += 1
                j += 1
            elif s[i][2] == 'R':
                stack.append([s[i][1], s[i][3]])
                i += 1
            else:
                x = [s[i][1], s[i][3]]
                while x[0] != 0 and len(stack) != 0:
                    if stack[-1][0] == x[0]:
                        stack.pop()
                        x[0] = 0
                    elif stack[-1][0] > x[0]:
                        stack[-1][0] -= 1
                        x[0] = 0
                    else:
                        x[0] -= 1
                        stack.pop()
                if x[0] != 0:
                    ans.append(x)
                i += 1
        i = 0
        while i < len(stack):
            ans.append(stack[i])
            i += 1
        ans = sorted(ans, key=lambda x: x[1])
        ans = [i[0] for i in ans]
        return ans
