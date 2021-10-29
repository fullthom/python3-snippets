import itertools


input = [[["A", "B"], ["C"]], [["D","E"],["F"]]]
for combos in itertools.product(*input):
    print(list(itertools.chain(*combos)))
