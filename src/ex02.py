import ex00

def signal(f):
    def wrapper(purse):
        print("SQUEAK")
        return f(purse)
    return wrapper

def main():
    purse:{str, int}  = {"aga:123": 123, "pupa": 1, "gold_ingots": 2, "uuuuu": 12}
    ex00.add_ingot = signal(ex00.add_ingot)
    ex00.get_ingot = signal(ex00.get_ingot)
    ex00.empty = signal(ex00.empty)
    print(ex00.add_ingot(purse))
    print(ex00.get_ingot(purse))
    print(ex00.empty(purse))

if __name__ == "__main__":
    main()