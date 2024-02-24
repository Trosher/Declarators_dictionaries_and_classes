def split_booty(*argv:list[dict:{str, int}]):
    goldAll = 0
    for dict_ in argv:
        if ("gold_ingots" in dict_ and dict_["gold_ingots"] > 0):
            goldAll += dict_["gold_ingots"]
    gold = goldAll // 3
    litelGold = goldAll % 3
    gold0 = goldAll // 3 + (litelGold == 2 if 1 else 0)
    gold1 = goldAll // 3 + (1 <= litelGold <= 2 if 1 else 0)
    return ({"gold_ingots", gold}, {"gold_ingots", gold0}, {"gold_ingots", gold1})
        

def main():
    purse:{str, int}  = {"aga:123": 122, "pupa": 1, "gold_ingots": 31, "uuuuu": 12}
    purse0:{str, int}  = {"aga:123": 123, "pupa": 1, "uuuuu": 12, "gold_ingots": 3}
    purse1:{str, int}  = {"gold_ingots": 2, "pupa": 1, "uuuuu": 12, "aga:123": 123}
    purse2:{str, int}  = {"aga:123": 123, "pupa": 1, "gold_ingots": 2, "uuuuu": 12}
    purse3:{str, int}  = {"aga:123": 123, "pupa": 1, "uuuuu": 12, "gold_ingots": 121}
    purse4:{str, int}  = {"gold_ingots": 1, "pupa": 1, "uuuuu": 12, "aga:123": 123}
    purse5:{str, int}  = {"pupa": 1, "uuuuu": 12, "aga:123": 123}
    print(split_booty(purse, purse0, purse1, purse2, purse3, purse4, purse5))

if __name__ == "__main__":
    main()