import random


class Deck:
    __deck_dic = {
        "A": 4,
        "2": 4,
        "3": 4,
        "4": 4,
        "5": 4,
        "6": 4,
        "7": 4,
        "8": 4,
        "9": 4,
        "10": 4,
        "J": 4,
        "Q": 4,
        "K": 4
    }
    __deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def pickCard(self):
        __card = ""
        __card_pick = random.choice(Deck.__deck)
        __hold = self.checkAvailable(__card_pick)
        if (__hold > 0):
            Deck.__deck_dic[__card_pick] -= 1
            __card = __card_pick
        else:
            for line in Deck.__deck:
                if Deck.__deck_dic[line] > 0:
                    Deck.__deck_dic[line] -= 1
                    __card = line
                    break
                else:
                    __card = "Deck is empty"
        return __card

    def checkAvailable(self, chosen):
        __tmp = Deck.__deck_dic[chosen]
        return __tmp

    def getDeck(self):
        return Deck.__deck_dic


"""
# driver
Player = Deck()
dealer = Deck()

print(dealer.getDeck())
"""
