
def add_value(map1):
    map1["1"].add(2)

a = set()
a.add(1)

map = {}
map["1"] = a

print(f"a = {a}, map = {map}")
add_value(map)
print(f"a = {a}, map = {map}")
# The second print shows 2 has been added.
