# Python3 program to Count of n digit numbers
# whose sum of digits equals to given sum
import math
 
def count(n, sum):
     
    # in case n = 2 start is 10 and
    # end is (100-1) = 99
    start = math.pow(10, n - 1);
    end = math.pow(10, n) - 1;
 
    count = 0;
    i = start;
     
    while(i <= end):
         
        cur = 0;
        temp = i;
         
        while(temp != 0):
            cur += temp % 10;
            temp = temp // 10;
         
        if(cur == sum):    
            count = count + 1;        
            i += 9;    
        else:
            i = i + 1;
         
    print(count);
 
# Driver Code
n = 3;
sum = 5;    
count(n, sum);
