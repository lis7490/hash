class HashTable:
    def __init__(self, size=10):

        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
    def _hash_function(self, key):

        return hash(key) % self.size

    def insert(self, key, value):

        if self.count >= self.size * 1:
            self._resize()

        hash_index = self._hash_function(key)
        bucket = self.table[hash_index]


        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return


        bucket.append((key, value))
        self.count += 1

    def search(self, key):

        hash_index = self._hash_function(key)
        bucket = self.table[hash_index]

        for k, v in bucket:
            if k == key:
                return v

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
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0


        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def __str__(self):

        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table))

ht = HashTable(size=5)

ht.insert("a", 1)
ht.insert("b", 2)
ht.insert("c", 3)
ht.insert("d", 4)
ht.insert("e", 5)
print("Before resize:")
print(ht)
print("Size:", ht.size)

ht.insert("f", 6)
ht.insert("g", 7)
ht.insert("h", 8)
ht.insert("k", 9)
ht.insert("l", 10)
print("\nAfter resize:")
print(ht)
print("Size:", ht.size)