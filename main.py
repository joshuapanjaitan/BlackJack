import deck


class Player:
    deck = deck.Deck()
    __bet = 10
    __bandar = 0

    def __init__(self, name):
        self.__name = name

    def getBet(self):
        return Player.__bet

    def alocateCard(self, count):
        __hasil = []
        __myCard = []
        i = 1
        while i <= count:
            tmp = Player.deck.pickCard()
            __myCard.append(tmp)
            i += 1
        hasil = [__myCard, self.countValue(__myCard)]
        print(__myCard)
        return hasil

    def countValue(self, setOfCard):
        __score = 0
        for line in setOfCard:
            if line == '10' or line == 'J' or line == 'Q' or line == 'K':
                __score += 10
            elif line == 'A':
                tmp = __score + 11
                if tmp <= 21:
                    __score += 11
                else:
                    __score += 1
            else:
                __score += int(line)

        return __score

    def setPlay(self, player, dealer):
        if player > dealer and player < 22:
            print("Kartu Player lebih tinggi")
        elif dealer > player:
            print("Kartu Dealer lebih tinggi")
        elif player > 21:
            print("Dealer lebih tinggi")
        else:
            print('imbang')

    def bet(self, bet):
        Player.__bet += bet

    def hit(self, input):
        print(self.__name+" Melakukan hit")
        __card = input[0]
        tmp = Player.deck.pickCard()
        __card.append(tmp)
        print(__card)
        return self.countValue(__card)

    def finish(self, player, dealer):
        if player > dealer and player == 21:
            Player.__bet *= 2
        elif player > dealer and player < 22:
            Player.__bet *= 1.5
        elif(player == dealer):
            pass
        else:
            Player.__bandar += Player.__bet
            Player.__bet -= Player.__bet


joice = Player('Joice')
Dealer = Player('Dealer')
joice.bet(100)
a = joice.alocateCard(2)
b = Dealer.alocateCard(2)

joice.setPlay(a[1], b[1])
hit1 = joice.hit(a)
joice.setPlay(hit1, b[1])

joice.finish(hit1, b[1])
print("Chips yang diperoleh :", joice.getBet())
