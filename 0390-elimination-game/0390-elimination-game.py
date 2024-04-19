class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        remaining = n
        step = 1
        head = 1
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
                
        
        return head
#         low = 1
#         high = n
        
#         arr = set(range(1, n+1))
        
#         start_from_max = False
        
#         jump = 2
        
#         while len(arr) != 1:
#             high = max(arr)
#             low = min(arr)
            
#             if start_from_max:
#                 i = high
#             else:
#                 i = low
            
#             while i <= high and i >= low:
#                 arr.remove(i)
#                 if start_from_max:
#                     i -= jump
#                 else:
#                     i += jump
            

#             start_from_max = not(start_from_max)            
#             jump = jump * 2

#         return list(set(arr))[0]