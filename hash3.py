def simple_string_hash(input_string):

    hash_value = 0
    for char in input_string:
        hash_value += ord(char)
    return hash_value

print(simple_string_hash("hello"))  # 532
print(simple_string_hash("world"))  # 552
print(simple_string_hash("Python"))  # 642
print(simple_string_hash(""))       # 0 (пустая строка)