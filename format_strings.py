
x = """
    test: {test}
"""
print(x.format(test="hello - keywords"))
try:
    print(x.format("hello - no keywords"))
except Exception as e:
    print("Running without keyword raised an exception!")
    print(e)
try:
    print(x.format(test="hello - keyword with invalid key too", foo="hello - this is an invalid keyword arg to the format string"))
except Exception as e:
    print("Running with an extra keyword raised an exception!")
    print(e)
