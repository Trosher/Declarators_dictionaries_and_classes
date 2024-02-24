def add_ingot(purse):
    res = purse.copy()
    try:
        res["gold_ingots"] += 1
    except Exception:
        res:{str, int} = {}
    return res

def get_ingot(purse):
    res=purse.copy()
    try:
        res["gold_ingots"] -= 1
        if res["gold_ingots"] < 0:
            res["gold_ingots"] = 0
    except Exception:
        res:{str, int} = {}
    return res
    
def empty(purse):
    res=purse.copy()
    try:
        res["gold_ingots"] -= res["gold_ingots"]
    except Exception:
        res:{str, int} = {}
    return res

def main():
    purse:{str, int}  = {"aga:123": 123, "pupa": 1, "gold_ingots": 2, "uuuuu": 12}
    purseErr:{str, int}  = {"aga:123": 123, "pupa": 1, "uuuuu": 12}
    print(add_ingot(purse))
    print(get_ingot(purse))
    print(empty(purse))
    print(add_ingot(purseErr))
    print(get_ingot(purseErr))
    print(empty(purseErr))

if __name__ == "__main__":
    main()