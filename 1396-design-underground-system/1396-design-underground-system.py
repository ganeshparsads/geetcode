from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.cities = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.cities[(self.customers[id][0], stationName)].append(t - self.customers[id][1])
        self.customers.pop(id, None)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.cities[(startStation, endStation)]) / len(self.cities[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)