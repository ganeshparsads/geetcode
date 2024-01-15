class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        never_lost = set()
        lost_1 = set()
        hash_lost = defaultdict()

        for i in matches:
            if i[0] not in hash_lost:
                hash_lost[i[0]] = 0
            if i[1] not in hash_lost:
                hash_lost[i[1]] = 0
            
            hash_lost[i[1]] += 1
        
        for key, val in hash_lost.items():
            if val == 0:
                never_lost.add(key)
            elif val == 1:
                lost_1.add(key)
        
        never_lost = list(never_lost)
        never_lost.sort()
        lost_1 = list(lost_1)
        lost_1.sort()
        return [never_lost, lost_1]