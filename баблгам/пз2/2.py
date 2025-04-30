def limited_hash(left=0, right=0, hash_function=hash):
    def hsh(obj):
        value = hash_function(obj)
        if left <= obj <= right:
            return obj
        else:
            lenght = right - left + 1
            return (value - left) % lenght + left
    return hsh


hash_function = limited_hash(10, 15)

print(hash_function(9))
print(hash_function(8))
print(hash_function(4))
print(hash_function(3))
print(hash_function(2))

a = 'U+5350'
print(chr(int(a[2:], 16)))