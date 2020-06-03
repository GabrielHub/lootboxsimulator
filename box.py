import json


# Loot box, odds are a dictionary ex. "rare": 0.04
class Box:
    def __init__(self, name, odds, pool):
        self.name = name
        self.odds = odds
        self.pool = pool  # contains all of the possible options
        self.droptable = None  # contains only the pullable items for this specific lootbox, list or dict

    def buildpool(self):
        pass

    def printdroptable(self):
        if self.droptable is None:
            print("Loot table is empty!")
        else:
            for i in self.droptable:
                print(i + " Drops:")
                print(self.droptable[i])


# basic item
class Item:
    def __init__(self, name):
        self.name = name


# MCOC item
class Champion(Item):
    def __init__(self, name, pic_id, u_id, basic4, basic5, basic6, feature5, feature6, star2, star3):
        super().__init__(name)  # display name
        self.pic_id = pic_id  # name that resolves to potrait filename - mattkraftid
        self.u_id = u_id  # unique id - champ number
        self.basic4 = basic4  # if not available, then a blank string
        self.basic5 = basic5
        self.basic6 = basic6
        self.feature5 = feature5
        self.feature6 = feature6
        self.star2 = star2  # 'y' for available, 'n' for no
        self.star3 = star3


#  basic cavalier crystal, 3* and 4* pools are the same
class CavCrystal(Box):
    def __init__(self, name, pool):
        super().__init__(name, {
            "star3": 0.5,
            "basic4": 0.38,
            "basic5": 0.11,
            "basic6": 0.01
            }, pool)
        self.droptable = {
            "star3": [],
            "basic4": [],
            "basic5": [],
            "basic6": []
        }
        self.buildpool()

    def buildpool(self):
        for champ in self.pool:
            if champ.basic4:
                self.droptable["star3"].append(champ)
                self.droptable["basic4"].append(champ)
            if champ.basic5:
                self.droptable["basic5"].append(champ)
            if champ.basic6:
                self.droptable["basic6"].append(champ)


# for mcoc example, creates the champion loot pool and returns the data
def mcoclootpool():
    ret = []  # list holds all champs

    # open json file
    with open("values.json", "r") as rfile:
        data = json.load(rfile)
    data = data["feed"]["entry"]

    # name, pic_id, u_id, basic4, basic5, basic6, feature5, feature6
    for i in data:
        if i["gsx$status"]["$t"] == "released":
            champ = Champion(i["gsx$champ"]["$t"], i["gsx$mattkraftid"]["$t"], i["gsx$champnumber"]["$t"], i["gsx$b"]["$t"], i["gsx$b_2"]["$t"], i["gsx$f"]["$t"], i["gsx$b_3"]["$t"], i["gsx$f_2"]["$t"], i["gsx$star_2"]["$t"], i["gsx$star_3"]["$t"])
            ret.append(champ)
    ret.reverse()
    return ret
