import json
import random


# contains loot pool + drop table to store in memory, g is the game of the pool to use
class Pool:
    def __init__(self, g):
        if g == 0:
            self.pool = self.mcoclootpool()  # to make it easier for portraits, dict of champ name: champ object
            self.droptable = self.mcocdroptable()

    # for mcoc example, creates the champion loot pool and returns the data
    def mcoclootpool(self):
        ret = {}  # list holds all champs

        # first load json to fill attributes corresponding to portrait file names, and unique ids

        # open json file
        with open("values.json", "r") as rfile:
            data = json.load(rfile)
        data = data["feed"]["entry"]  # cut out gsheet formatting

        # name, pic_id, u_id, basic4, basic5, basic6, feature5, feature6
        for i in data:
            if i["gsx$status"]["$t"] == "released":
                ret[i["gsx$champ"]["$t"]] = Champion(i["gsx$champ"]["$t"], i["gsx$mattkraftid"]["$t"], i["gsx$champnumber"]["$t"], i["gsx$star_2"]["$t"], i["gsx$star_3"]["$t"])
        return ret

    # build the possible drop tables
    def mcocdroptable(self):
        ret = {
            "2star": [],
            "3star": [],
            "4star": [],
            "5basic": [],
            "5feature": [],
            "6basic": [],
            "6feature": []
        }

        # get the 2 and 3 star values from  champ data first
        # these are just the total 2 and 3* pools, the actual crystal droptable IS THE SAME AS THE 4* BASIC
        # commented out
        """for champ in self.pool:
            if champ.star2 == "y":
                ret["2star"].append(champ.name)
            if champ.star3 == "y":
                ret["3star"].append(champ.name)"""

        # rest of the data is stored in seperate file, kept as Champ.name
        with open("pool.json", "r") as rfile:
            data = json.load(rfile)
        data = data["feed"]["entry"]  # skip gsheet formatting to inputs

        # for basic 4, 5, 6 and feature 5, 6 - seperated manually by cell columns in gsheet
        # if col doesn't match, do nothing because it's probably garbo data
        # was gonna use a switch statement but that seemed to complex for a second part of this method
        for i in data:
            # tofix: is comparing strings faster than converting a string of a number back to an int?
            if i["gs$cell"]["col"] == '3':
                # feature5
                ret["5feature"].append(i["gs$cell"]["$t"])
            elif i["gs$cell"]["col"] == '5':
                # basic5
                ret["5basic"].append(i["gs$cell"]["$t"])
            elif i["gs$cell"]["col"] == '7':
                # feature6
                ret["6feature"].append(i["gs$cell"]["$t"])
            elif i["gs$cell"]["col"] == '11':
                # basic4
                ret["4star"].append(i["gs$cell"]["$t"])
                ret["2star"].append(i["gs$cell"]["$t"])  # added here b/c i think this works better
                ret["3star"].append(i["gs$cell"]["$t"])
            elif i["gs$cell"]["col"] == '17':
                # basic6
                ret["6basic"].append(i["gs$cell"]["$t"])

        # for other specialty crystals, an inherited class should overload this method
        return ret

    # given the name of a champ, return the pic_id
    def mcocgetpotrait(self, name):
        return self.pool[name].pic_id

    def printdroptable(self):
        if self.droptable is None:
            print("Loot table is empty!")
        else:
            for i in self.droptable:
                print("\n", i, str(len(self.droptable[i])), "Drops:")
                for j in self.droptable[i]:
                    print(j)


# Loot box, odds are a dictionary ex. "rare": 0.04
class Box:
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    # given the droptable
    def spin(self, table):
        # pick rarity gets the rarity of the item first, based off the weighted odds
        pick_rarity = random.choices(list(self.odds.keys()), list(self.odds.values()))[0]

        # assuming the items in a rarity pool have equal weight, now pick from weighted pool except for first index
        # first index contains extra info about the pool, ex. command, number of hamps in table, and % of each
        pick_from_rarity = random.choice([x for index, x in enumerate(table[pick_rarity]) if index != 0])
        return pick_from_rarity, pick_rarity[0] + " star"

    def reelspin(self, table):
        pass


# basic item
class Item:
    def __init__(self, name, u_id):
        self.name = name  # display name
        self.u_id = u_id  # unique id -


# MCOC item
class Champion(Item):
    def __init__(self, name, pic_id, u_id, star2, star3):
        super().__init__(name, u_id)
        self.pic_id = pic_id  # name that resolves to potrait filename - mattkraftid
        self.star2 = star2  # 'y' for available, 'n' for no
        self.star3 = star3


#  basic cavalier crystal, 3* and 4* pools are the same I think
class CavCrystal(Box):
    # manually add the odds for each crystal type
    def __init__(self):
        super().__init__("Cavalier Crystal", {
            "3star": 0.5,
            "4star": 0.38,
            "5basic": 0.11,
            "6basic": 0.01
            })


#  basic grand master crystal, 3* and 4* pools are the same I think
class GMC(Box):
    # manually add the odds for each crystal type
    def __init__(self):
        super().__init__("Grandmaster Crystal", {
            "3star": 0.82,
            "4star": 0.15,
            "5basic": 0.03
            })


# featured cav crystal, with input for multitude of featured champs
class FeatCavCrystal(CavCrystal):
    pass
