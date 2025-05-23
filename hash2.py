class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        if self.count >= self.size:
            self._resize()
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.count += 1

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        hash_index = self._hash_function(key)
        bucket = self.table[hash_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def _resize(self):
        old_table = self.table
        old_size = self.size
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        for bucket in old_table:
            if bucket is not None:
                for pair in bucket:
                    self.insert(pair[0], pair[1])

table = HashTable(size=5)

table.insert("a", 1)
table.insert("b", 2)
table.insert("c", 3)
table.insert("d", 4)
table.insert("e", 5)
print("До увеличения:")
print("Size:", table.size)

table.insert("f", 6)
table.insert("g", 7)
table.insert("h", 8)
table.insert("k", 9)
table.insert("l", 10)
print("После увеличения:")
print("Size:", table.size)