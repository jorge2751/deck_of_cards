# "hit" = draw a card
# "stand" = stop drawing cards
# track your total points
# PLAYER = initates hand and adds cards/their points to hand
from . import card
from . import deck

class Player:
    def __init__(self):
        self.hand = []
        self.points = 0

    def take_card(self, card):
        #remove card from top of deck and add to hand
        self.hand.append(card.card_info())
        self.points += card.card_val()
        return self

    def display_cards(self):
        print(self.hand)
        return self

    def display_points(self):
        print(self.points)
        return self

    def auto_draw(self, card):
        if self.points < 17:
            self.take_card(card)
        else:
            pass
        return self
