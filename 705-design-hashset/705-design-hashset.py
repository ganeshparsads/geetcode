class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.bucketItems = 1000
        self.store = [False for x in range(1000)]


    def bucket(self, key):
        return key%self.buckets

    def bucketItem(self, item):
        return item // self.bucketItems
        
    def add(self, key: int) -> None:
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        
        if not self.store[bucket]:
            if bucket == 0:
                self.store[bucket] = [False for x in range(self.bucketItems+1)]
            else:
                self.store[bucket] = [False for x in range(self.bucketItems)]
        
        self.store[bucket][bucketItem] = True

    def remove(self, key: int) -> None:
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        
        if not self.store[bucket]:
            return
        self.store[bucket][bucketItem] = False


    def contains(self, key: int) -> bool:
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        
        if not self.store[bucket]:
            return False
        elif not self.store[bucket][bucketItem]:
            return False
        else:
            return self.store[bucket][bucketItem]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)