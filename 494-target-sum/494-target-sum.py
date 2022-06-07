class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def countSubsestSum(nums, S):
            n = len(nums)
            t = [[0]*(S+1) for i in range(n+1)]
            t[0][0] = 1            
            for i in range(1, n+1):
                for j in range(S+1):
                    if (nums[i - 1] <= j):
                        t[i][j] = t[i - 1][j - nums[i - 1]] + t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j]
            return t[n][S]
        
        sumArr = sum(nums)
        diff = target
        if(((sumArr - target) % 2 != 0) or (target > sumArr)):
            return 0
        S2 = (sumArr - diff) // 2
        
        return countSubsestSum(nums, S2)
