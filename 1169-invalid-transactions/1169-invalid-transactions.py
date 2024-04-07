class Solution:
    def get_str(self, trans):
        return "{},{},{},{}".format(trans["name"], trans["time"], trans["amt"], trans["city"])
    
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ts = []
        for t in transactions:
            trans = t.split(",")
            dict_trans = {
                "name": trans[0],
                "time": int(trans[1]),
                "amt": int(trans[2]),
                "city": trans[3]
            }
            ts.append(dict_trans)
        
        ts = sorted(ts, key=lambda x: x['time'])
        
        name2q = defaultdict(lambda: deque())
        
        ans = []
        invalid = [False] * len(ts)
        
        for i in range(len(ts)):
            name = ts[i]["name"]
            time = ts[i]["time"]
            amt = ts[i]["amt"]
            city = ts[i]["city"]
            q = name2q[name]
            while q and time - q[0][0] > 60:
                q.popleft()

            cur_invalid = amt > 1000

            for _, other_city, j in q:
                if city != other_city:
                    cur_invalid = True
                    if not invalid[j]:
                        invalid[j] = True
                        ans.append(self.get_str(ts[j]))
            if cur_invalid:
                invalid[i] = True
                ans.append(self.get_str(ts[i]))

            name2q[name].append((time, city, i))

        return ans        
        