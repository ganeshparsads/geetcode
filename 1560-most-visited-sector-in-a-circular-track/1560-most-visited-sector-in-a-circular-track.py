class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        counter = defaultdict(int)
        for i in range(len(rounds)-1):
            if i==0:
                cur = rounds[i]-1
                counter[cur] += 1
            while cur != rounds[i+1]-1:
                cur = (cur+1)%n
                counter[cur] += 1
        most = max(counter.values())
        res = []
        for i in counter:
            if counter[i] == most:
                res.append(i+1)
        return sorted(res)