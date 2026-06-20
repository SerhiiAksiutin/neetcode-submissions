class Pair:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        hashIndex = key % self.capacity

        if self.table[hashIndex] and self.table[hashIndex].key != key:
            while self.table[hashIndex]:
                hashIndex = (hashIndex + 1) % self.capacity
        
        self.table[hashIndex] = Pair(key, value)
        self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()        

    def get(self, key: int) -> int:
        hashIndex = key % self.capacity
        
        while self.table[hashIndex]:
            pair = self.table[hashIndex]
            if pair.key == key:
                return pair.val
            hashIndex = (hashIndex + 1) % self.capacity
        
        return -1

    def remove(self, key: int) -> bool:
        hashIndex = key % self.capacity

        while self.table[hashIndex]:
            pair = self.table[hashIndex]
            if pair.key == key:
                self.table[hashIndex] = None
                self.size -= 1
                return True
            hashIndex = (hashIndex + 1) % self.capacity
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.size = 0
        self.capacity *= 2
        newTable = [None] * self.capacity

        oldTable = self.table
        self.table = newTable

        for entry in oldTable:
            if entry:
                hasIndex = entry.key % self.capacity
                self.insert(entry.key, entry.val)

