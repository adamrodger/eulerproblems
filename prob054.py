VALUES = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
SUITS = {"C":0, "D":1, "H":2, "S":4}

class Card(object):
    def __init__(self, repr):
        self.value = repr[0]
        self.suit = repr[1]
        self.numvalue = VALUES[repr[0]]

    def __repr__(self):
        return self.value + self.suit
        
    def __lt__(self, other):
        if self.numvalue == other.numvalue:
            return SUITS[self.suit] < SUITS[other.suit]
        return self.numvalue < other.numvalue
        
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit
        
    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not (self.__lt__(other) or self.__eq__(other))

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
        
class PokerHand(object):
    def __init__(self, cards):
        self.cards = cards
        
    def _royal_flush(self):
        """ Straight and flush and highest card is Ace """
        if self._straight() and self._flush() and (sorted(self.cards)[-1].numvalue == 14):
            return (1 << 23) + SUITS[sorted(self.cards)[-1].suit]
        else:
            return None
    
    def _straight_flush(self):
        """ Straight and flush """
        if self._straight() and self._flush():
            return (1 << 22) + SUITS[sorted(self.cards)[-1].suit]
        else:
            return None
        
    def _four_kind(self):
        """ 4 occurrences of a value in the set of card vals """
        vals = [card.value for card in self.cards]
        setvals = set(vals)
        for val in setvals:
            if vals.count(val) == 4:
                result = (1 << 21)
                if val > 2:  
                    result += (1 << val)
                return result
        return None

    def _full_house(self):
        """ A 3 and 2 of a kind in the set of card vals """
        vals = [card.numvalue for card in self.cards]
        setvals = set(vals)
        pair = False
        three = False
        
        for val in setvals:
            if vals.count(val) == 3:
                three = val
            elif vals.count(val) == 2:
                pair = val
            else:
                return None
                
        if pair and three:
            return (1 << 20) + (1 << three)
        else:
            return None

    def _flush(self):
        """ Only 1 value in the set of card sets """
        if 1 == len(set(card.suit for card in self.cards)):
            return (1 << 19) + (1 << sorted(self.cards)[-1].numvalue) + SUITS[sorted(self.cards)[-1].suit]
        else:
            return None

    def _straight(self):
        vals = sorted([card.numvalue for card in self.cards])
        if vals == range(vals[0], vals[0] + 5):
            return (1 << 18) + (1 << sorted(self.cards)[-1].numvalue)
        else:
            return None
        
    def _three_kind(self):
        vals = [card.numvalue for card in self.cards]
        setvals = set(vals)
        for val in setvals:
            if vals.count(val) == 3:
                return (1 << 17) + (1 << val)
        return None
        
    def _pairs(self):
        vals = [card.numvalue for card in self.cards]
        setvals = set(vals)
        pairs = []
        for val in setvals:
            if vals.count(val) == 2:
                pairs.append(val)
        return pairs
        
    def _two_pair(self):
        result = sorted(self._pairs())
        if len(result) == 2:
            return (1 << 16) + (1 << result[1]) + (1 << result[0])
        else:
            return None
        
    def _one_pair(self):
        result = sorted(self._pairs())
        if len(result) == 1:
            return (1 << 15) + (1 << result[0])
        else:
            return None
        
    def _highest_card(self):
        vals = sorted(set([card.numvalue for card in self.cards]))
        total = 0
        for val in vals:
            if val > 2:
                total += 1 << val
        return total
        
    RULES = [_royal_flush, _straight_flush, _four_kind, _full_house, _flush, _straight, _three_kind, _two_pair, _one_pair, _highest_card]
        
    def hand_result(hand):
        for rule in PokerHand.RULES:
            result = rule(hand)
            if result != None:
                return result
        
    def __eq__(self, other):
        result1 = PokerHand.hand_result(self)
        result2 = PokerHand.hand_result(other)
        
        if result1 == result2:
            print "\t", result1, "vs", result2, "DRAW"
        
        return result1 == result2
        
    def __lt__(self, other):
        result1 = PokerHand.hand_result(self)
        result2 = PokerHand.hand_result(other)
        
        if result1 < result2:
            print "\t", result1, "vs", result2, "LOSE"
        elif result1 > result2:
            print "\t", result1, "vs", result2, "WIN"
        
        return result1 < result2
        
    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not (self.__lt__(other) or self.__eq__(other))

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
            
if __name__ == "__main__":
    f = open("Data/poker.txt", "r")
    games = [(cards.split(" ")[:5], cards.replace("\n", "").split(" ")[5:]) for cards in f]
    hands = []
    for game in games:
        hand1 = sorted([Card(x) for x in game[0]])
        hand2 = sorted([Card(x) for x in game[1]])
        hands.append((PokerHand(hand1), PokerHand(hand2)))
    
    print len([hand for hand in hands if hand[0] > hand[1]])
    
    #output = open("Data/prob054.out.txt", "w")
    #import sys
    #sys.stdout = output
    
    #for hand in hands[:]:
    #    print hand[0].cards, hand[1].cards, "" if hand[0] < hand[1] else "" if hand[0] == hand[1] else ""
    
    #output.close()