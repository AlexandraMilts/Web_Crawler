def find_last(a,b):
    last_pos = -1
    while True:
        pos = a.find(b, last_pos+1)
        if pos == -1:
            return last_pos
        last_pos = pos

print
find_last('aaaa', 'a')
# >>> 3

# print find_last('aaaaa', 'aa')
# >>> 3

print
find_last('aaaa', 'b')
# >>> -1

# print find_last("111111111", "1")