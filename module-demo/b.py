# Prints "b.py" so we know when the file in this code was called
print("b.py")

# A function we can call to test out the import
def run():
    print("b.py run")


# A class we can import
class B(object):
    def __init__(self):
        print("class B __init__()")
