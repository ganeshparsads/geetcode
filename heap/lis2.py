class Solution:    

    def helper(self,sub,x):
        l = 0 
        r = len(sub)-1
        ans = l 
        while(l <= r):
            
            mid = l + (r-l)//2
            
            if(sub[mid] == x):
                
                return mid 
            
            elif(sub[mid] < x):
                
                l = mid + 1 
            
            else:
                ans = mid 
                r = mid - 1
        
        return ans

    def helperR(self,sub,x):
        l = 0
        r = len(sub)-1
        ans = r
        while(l <= r):
            mid = l + (r-l)//2
            if(sub[mid] == x):
                return mid 
            elif(sub[mid] > x):
                ans = mid
                l = mid + 1 
            else:
                r = mid - 1
        
        return ans

    def lengthOfLIS(self, arr, k) -> int:
        sub = []
        for i, x in enumerate(arr):
            if len(sub) == 0 or sub[-1] < arr[i] and abs(sub[-1]-arr[i]) <= k:  
                sub.append(x)
            elif(sub[-1] == arr[i]):
                continue
            else:
                idx = self.helper(sub, x)
                print(self.helperR(sub, x))
                sub[idx] = x 
        print(sub)
        return len(sub)

obj = Solution()

print(obj.lengthOfLIS([1,4,7,15,5], 1))
