from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            val = self.array[key]
            del self.array[key]
            self.array[key] = val
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            del self.array[key]
        elif len(self.array) == self.capacity:
            self.array.popitem(last=False)
  
        self.array[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            val = self.array[key]
            del self.array[key]
            self.array[key] = val
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            del self.array[key]
        elif len(self.array) == self.capacity:
            self.array.popitem(last=False)
  
        self.array[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)