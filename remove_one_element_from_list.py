
def get_lists_with_one_removed(x):
    res = []
    for i in range(len(x)):
        res.append(x[0:i] + x[i + 1:])
    return res


def run(x):
    print("Running for list with length {}".format(x))
    print("Original list:")
    o = list(range(x))
    print("Lists with 1 removed:")
    for i in get_lists_with_one_removed(o):
        print(i)

run(4)
run(5)
run(1)
run(0)
