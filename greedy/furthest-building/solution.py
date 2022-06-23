class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        cnt = 0
        size = len(heights)

        for idx, i in enumerate(heights):
            if idx == 0:
                continue
 
            if idx == size-1:
                print("Hello", i, idx)
                break

            if not bricks and not ladders:
                break

            print("Hi")
            print(idx)
            cnt += 1

            if i >= heights[idx+1]:
                continue

            if i < heights[idx+1]:
                if idx == 7:
                    import pdb
                    pdb.set_trace()

                diff = heights[idx+1] - i
                if bricks and bricks >= diff:
                    bricks = bricks - diff
                elif ladders:
                    ladders = ladders - 1
                else:
                    print("Hi")
                    return cnt

        return cnt

obj = Solution()

print(obj.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))
