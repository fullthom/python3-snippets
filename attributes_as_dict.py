
class Tester:
    def __init__(self):
        self.a = "a"
        self.x = None    
    def b(self):
        return 100

    def get_as_dict(self):
       return vars(self)
tester = Tester()
print("vars(tester) = {}".format(vars(tester)))
print("tester.get_as_dict() = {}".format(tester.get_as_dict()))
