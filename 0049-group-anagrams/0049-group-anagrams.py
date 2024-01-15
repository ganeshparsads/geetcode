from itertools import groupby

class Solution:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269]

    # get a unique integral hash based on the quantity we have
    @staticmethod
    def strHash(s):
        sh = 1
        for c in s:
            sh *= Solution.primes[ord(c)-ord('a')]
        return sh

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outdict = {}
        for string in strs:
            ha = Solution.strHash(string)
            if ha not in outdict:
                outdict[ha] = [string]
            else:
                outdict[ha].append(string)

        return outdict.values()
