
def run():
    should_run = True
    while should_run:
        print("should run!")    
        for i in range(0, 5):
            for j in range(0, 5):
                if j % 2 == 0:
                    continue
                print("\t" + str(j))
            print(str(i))
        else:
            print("woah!")
            should_run = False

run()
