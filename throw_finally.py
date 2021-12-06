

def run(should_raise):
    try:
        print("In start of try")
        if should_raise:
            raise Exception("Exception raised from try")
        print("End of try")
    except Exception as e:
        print("Start of except")
        raise Exception("Raising in except") from e
        print("end of except")
    finally:
        print("finally")


print("Running without raising:")
run(False)
print()
print("Running with raising")
run(True)
