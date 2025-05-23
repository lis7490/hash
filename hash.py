from operator import index


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
    def hash_function(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                return pair
        self.table[index].append([key, value])
    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None
    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index].pop(i)
                    return True
        return False


table = HashTable(10)
table.insert('car', 10)
table.insert('motorcycle', 20)
table.insert('cycle', 30)
table.insert('plane', 40)
print(table.search('cycle'))
table.delete("motorcycle")
print(table.search('motorcycle'))
print(table.search('plane'))




