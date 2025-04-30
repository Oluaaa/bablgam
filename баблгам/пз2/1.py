def hash_function(obj):
    obj = str(obj)
    count = 0
    tot = 1
    temp1 = 0
    temp2 = 0
    if len(obj) % 2 == 0:
        for i in range(len(obj) // 2):
            temp1 += (ord(obj[i]) * ord(obj[0 - i - 1]))
    else:
        for i in range(len(obj) // 2):
            temp1 += (ord(obj[i]) * ord(obj[0 - i - 1]))
        temp1 += ord(obj[len(obj) // 2])

    for i in range(len(obj)):
        if count == 0:
            temp2 += ord(obj[i]) * tot
            tot += 1
            count += 1
        else:
            temp2 -= ord(obj[i]) * tot
            tot += 1
            count -= 1
    return (temp1 * temp2) % 123456791


print(hash_function('python'))
#111998846
print(hash_function(12345))
print(hash_function(None))