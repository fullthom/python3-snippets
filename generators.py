def generate_ints(start, end):
    n = start
    while n < end:
        yield n
        n += 1

for i in generate_ints(0, 10):
    print(i)

"""
0
1
2
3
4
5
6
7
8
9
"""
