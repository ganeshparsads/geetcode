class Solution:

    def getMax(self, height):
        maxLIndices = []
        maxL = 0
        for val in height:
            maxL = max(maxL, val)
            maxLIndices.append(maxL)
        return maxLIndices

    def trap(self, height):
        maxLIndices = self.getMax(height)
        maxRIndices = list(reversed(self.getMax(reversed(height))))

        total = 0

        for idx, val in enumerate(height):
            total += min(maxRIndices[idx], maxLIndices[idx]) - val

        return total
