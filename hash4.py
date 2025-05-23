def simple_string_hash(input_string):

    return sum(ord(char) for char in input_string)


class HashDictionary:
    def __init__(self, size=10):

        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _get_index(self, key):

        return simple_string_hash(key) % self.size

    def insert(self, key, value):

        if self.count >= self.size * 0.7:
            self._resize()

        index = self._get_index(key)
        bucket = self.table[index]


        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return


        bucket.append((key, value))
        self.count += 1

    def search(self, key):

        index = self._get_index(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def _resize(self):

        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0


        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def __contains__(self, key):

        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __str__(self):

        items = []
        for bucket in self.table:
            for key, value in bucket:
                items.append(f"'{key}': {value}")
        return "{" + ", ".join(items) + "}"



if __name__ == "__main__":
    hd = HashDictionary()

    # Добавление элементов
    hd.insert("apple", 10)
    hd.insert("banana", 20)
    hd.insert("orange", 30)
    print("Словарь после добавления:", hd)

    # Поиск элементов
    print("Значение для 'apple':", hd.search("apple"))
    print("Значение для 'banana':", hd.search("banana"))

    # Проверка наличия ключа
    print("Есть ли 'orange'?", "orange" in hd)
    print("Есть ли 'grape'?", "grape" in hd)

    # Обновление значения
    hd.insert("apple", 15)
    print("Обновленное значение для 'apple':", hd.search("apple"))

    # Попытка поиска несуществующего ключа
    try:
        print(hd.search("grape"))
    except KeyError as e:
        print("Ошибка:", e)