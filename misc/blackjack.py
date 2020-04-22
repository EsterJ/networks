from random import randint, seed
# performance of just the dealer strategy: 0.453428


def deal():
    # returns value of card dealt, faces cards are 10, aces are 11
    cardId = randint(2, 14)
    if cardId < 11:
        return cardId
    elif 11 <= cardId < 14:
        return 10
    else:
        return 11


class Player:
    def __init__(self):
        self.total = 0
        self.aces = 0
        self.dealerTotal = 0
        self.dealerAces = 0
        # num of aces is num of "soft" aces (can only be 0 or 1)

    def reset(self):
        self.__init__()

    def hit(self):
        # 'hit' player and update state variable accordingly
        # returns True if the hit results in a bust, False otherwise
        cardValue = deal()
        self.total += cardValue
        if cardValue == 11:
            self.aces += 1

        # check if we're over 21
        if self.total > 21:
            # if we have an ace, turn the ace to a one
            if self.aces > 0:
                self.total -= 10
                self.aces -= 1
            else:
                return True
        return False

    def strategy(self):
        # based on state variables, decide whether to hit or stand; return true for a hit
        if self.total < 17:
            return True
        return False

    def play_hand(self):
        # plays a hand against dealer, returns 1 if won, 0 if lost, 0.5 if tied

        self.__init__()
        self.dealerTotal = deal()

        if self.dealerTotal == 1:
            self.dealerAces = 1

        # hit until player decides to stop
        while self.strategy():
            if self.hit():
                return 0  # player loses if bust

        # hit dealer until dealer decides to stop
        while self.dealerTotal < 17:
            dealerCardValue = deal()
            if dealerCardValue == 11:
                self.dealerAces += 1
            self.dealerTotal += dealerCardValue

            # check if the dealer busted
            if self.dealerTotal > 21:
                if self.dealerAces > 0:  # if there are aces, turn an ace hard
                    self.dealerTotal -= 10
                    self.dealerAces -= 1
                else:
                    return 1  # player wins if dealer busts

        if self.total > self.dealerTotal:
            return 1
        elif self.total == self.dealerTotal:
            return 0.5
        else:
            return 0


if __name__ == '__main__':
    numOfTests = 100
    seed(1)  # seed random number generator
    myPlayer = Player()
    wins = 0

    for i in range(numOfTests):
        wins += myPlayer.play_hand()

    print(wins/numOfTests)
