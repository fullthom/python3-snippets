import traceback

def run1():
    run2()

def run2():
    run3()

def run3():
    run4()

def run4():
    print(1 / 0)

def handle_exp(e):
    print(traceback.format_exc())


try:
    run1()
except Exception as e:
    handle_exp(e)
