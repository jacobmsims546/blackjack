# Blackjack
# Made by Jacob Simmons ()
import random
print(""" 
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                       _/ |                
                      |__/  
      
A classic and thrilling game of chance.
Enter "start" to begin. Enter "rules" for an explanation of the rules.
Type "reset" at any time to reset this game entirely and return to this title.
""")
terminalin = input("---> ")
if terminalin == "rules":
    print("""
        Blackjack is a simple and popular card game of chance played around the world.

        The object of the game is to win money by creating card totals higher than those of the dealer's
        hand but not exceeding 21, or by stopping at a total in the hope that the dealer will bust (exceed a hand value of 21).

        The value of a hand is the sum of the numbered cards, with face cards (jacks, queens, kings) carrying a value of 10.
        Ace cards have either a value of 1 or 11, depending on the players' choice.

        The player starts by making a bet on the next game.
        The player is then dealt a hand of two cards, while the dealer starts with a hand of one card.

        On their turn, the player may choose to "hit" (take a card and continue their turn), "stand" (end their turn without taking a card), "double" 
        (double their wager, take a single card, and end their turn), "split" (only if the two cards in the starting hand have the same value, separate them to make two hands),
        or "surrender" (forfeit half of your bet to retire from the game, this is only available as the first action of a player's turn).

        If a player chooses to "split" their starting hand, Each new hand gets a second card resulting in two starting hands. This requires an additional bet on the second hand. 
        The two hands are played out independently, and the wager on each hand is won or lost independently. 
        In the case of cards worth 10 points, splitting is only allowed when the cards rank the same. For example, 10-10 could be split, but K-10 could not.
        Doubling and re-splitting after splitting once is not allowed. A 10-valued card and an ace resulting from a split isn't considered a blackjack (hand value of exactly 21).

        Once the player is finished with their turn, the dealer resolves their hand by drawing until their hand total is 17 or above, or if they exceed 21 (a bust).
        If the dealer busts, the player wins regardless of the value of their hand. 
        If the value of the dealer's hand is closer to 21 than the player's, the dealer wins. 
        The opposite is true if the player's hand is closer to 21 than the dealer's, resulting in a win for the player.
        The player automatically loses if their hand exceeds a value of 21 during their turn (a bust).

        If the player wins the hand, they recieve money at a ratio of 3:2 of their bet for that round as winnings.
        Upon a loss, the player loses the money that they have betted for that round.
        """)
    terminalin = input("---> ")

if terminalin == "start":
    print("Starting play...")
    print("Total Cash = $500", "Hands Played = 0")
    print("How much money would you like to bet on this hand?")
    bet = input("---> ")

while terminalin != "start" and terminalin != "rules":
    print("Sorry, it looks like you haven't chosen \"start\" or \"rules\".")
    terminalin = input("---> ")

masterdeck = {["Ace", [1, 11]], ["Ace", [1, 11]], ["Ace", [1, 11]], ["Ace", [1, 11]], ["One", 1], ["One", 1], ["One", 1], ["One", 1], ["Two", 2], ["Two", 2], ["Two", 2], ["Two", 2], ["Three", 3],
              ["Three", 3], ["Three", 3], ["Three", 3], ["Four", 4], ["Four", 4], ["Four", 4], ["Four", 4], ["Five", 5], ["Five", 5], ["Five", 5], ["Five", 5], ["Six", 6], ["Six", 6], ["Six", 6]
              ["Six", 6], ["Seven", 7], ["Seven", 7], ["Seven", 7], ["Seven", 7], ["Eight", 8], ["Eight", 8], ["Eight", 8], ["Eight", 8], ["Nine", 9], ["Nine", 9], ["Nine", 9], ["Nine", 9],
              ["Ten", 10], ["Ten", 10], ["Ten", 10], ["Ten", 10], ["Jack", 10], ["Jack", 10], ["Jack", 10], ["Jack", 10], ["Queen", 10], ["Queen", 10], ["Queen", 10], ["Queen", 10],
              ["King", 10], ["King", 10], ["King", 10], ["King", 10]}

dealerhand = []
playerhand = []
