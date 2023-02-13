from classes.deck import Deck
from classes.player import Player
# from classes.dealer import Dealer

bicycle = Deck()

bicycle.shuffle_cards()

dealer = Player()
player1 = Player()
dealer.auto_draw(bicycle.cards.pop()).auto_draw(bicycle.cards.pop())
player1.take_card(bicycle.cards.pop()).take_card(bicycle.cards.pop())

player1.display_cards().display_points()
while 1 > 0:
    if player1.points > 21:
        print("You Lose!")
        break

    move = input("Hit or Stand?")

    if move == "Hit":
        player1.take_card(bicycle.cards.pop())
        player1.display_cards().display_points()
        dealer.auto_draw(bicycle.cards.pop())
    elif move == "Stand":
        dealer.auto_draw(bicycle.cards.pop()).auto_draw(bicycle.cards.pop()).auto_draw(bicycle.cards.pop()).auto_draw(bicycle.cards.pop())
        dealer.display_cards().display_points()
        if player1.points == dealer.points:
            print("Draw!")
        elif player1.points > dealer.points:
            print("You Win!")
        elif dealer.points > 21:
            print("You Win!")
        else:
            print("You Lose!")
        break