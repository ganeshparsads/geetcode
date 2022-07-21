class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        start = 0
        end = len(A) - 1
        res = -1

        while start <= end:
            mid = start + (end - start) // 2

            ele = A[mid]

            if ele == X:
                return ele

            elif ele < X:
                res = ele
                start = mid + 1

            else:
                end = mid - 1

        return -1

obj = Solution()

print(obj.findFloor([1,2,8,10,11,12,19], 7, 5))
