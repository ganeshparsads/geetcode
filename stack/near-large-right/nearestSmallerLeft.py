class Solution:
    """
    prob: 496 => https://leetcode.com/problems/next-greater-element-i/
    """
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        g_map = {}
        for num in nums2:
            # if num == 1:
            #     import pdb
            #     pdb.set_trace()

            if not stack:
                stack.append(num)
                g_map[num] = -1
                continue

            if stack[-1] > num:
                g_map[num] = stack[-1]
                stack.append(num)

            else:
                while stack and stack[-1] <= num:
                    print(stack.pop())

                if not stack:
                    g_map[num] = -1
                else:
                    g_map[num] = stack[-1]

                stack.append(num)

        print(g_map)

        return [g_map[x] for x in nums1]
