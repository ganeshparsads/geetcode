class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        tens = 1
        result = 0 
        
        for j in range(len(num2)-1, -1, -1):
            tempSum = 0
            tempTens = 1
            for i in range(len(num1)-1, -1, -1):
                prd = int(num1[i])*int(num2[j])
                prd *= tempTens
                tempSum += prd
                tempTens *= 10

            result += tempSum * tens
        
            tens *= 10
        
        return str(result)