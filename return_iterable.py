import itertools

def return_iterable():
    return itertools.combinations(["A", "B", "C"], 2)

for i in return_iterable():
    print(i)
"""
('A', 'B')
('A', 'C')
('B', 'C')


I wanted to see if I could do a return like this or had to
wrap the iterable in my own loop and have yield statement.
This works though so I don't need to do that.
"""
   
