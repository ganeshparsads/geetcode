class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tracer = list()
        self.data = dict()

    def get(self, key: int) -> int:
        if key in self.tracer:
            self.tracer.remove(key)
            self.tracer.append(key)

        return self.data.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.tracer:
            self.tracer.remove(key)

        elif len(self.tracer) == self.capacity:
            e_key = self.tracer.pop(0)
            print("Evicted: ", e_key)
            del self.data[e_key]

        self.tracer.append(key)
        self.data[key] = value
