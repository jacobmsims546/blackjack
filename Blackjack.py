# Blackjack
# Made by Jacob Simmons
import random

def title():
    print(""" 
     _      _            _    _            _    
    | |    | |          | |  (_)          | |   
    | |__  | | __ _  ___| | ___  __ _  ___| | __
    | '_ \ | |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_)  | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/ |_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                           _/ |                
                          |__/  
      
    A classic card game of chance.
    Coded by Jacob Simmons (@jacobmsims546 on GitHub)
    Enter "start" to begin. Enter "rules" for an explanation of the rules.
    """)

def start(terminalin):
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
            (double their wager, take a single card, and end their turn), or "split" (only if the two cards in the starting hand have the same value, separate them to make two hands).
              
            A player may only choose to double on their turn if they have not split, they have recieved two cards, and they have not chosen to hit yet.

            If a player chooses to "split" their starting hand, each new hand gets a second card resulting in two starting hands. This requires an additional bet on the second hand. 
            The two hands are played out independently, and the wager on each hand is won or lost independently. 
            In the case of cards worth 10 points, splitting is only allowed when the cards rank the same. For example, 10-10 could be split, but K-10 could not.
            Doubling and re-splitting after splitting once is not allowed. A 10-valued card and an ace resulting from a split isn't considered a blackjack (hand value of exactly 21).

            Once the player is finished with their turn, the dealer resolves their hand by drawing until their hand total is 17 or above, or if they exceed 21 (a bust).
            If the dealer busts, the player wins regardless of the value of their hand. 
            If the value of the dealer's hand is closer to 21 than the player's, the dealer wins. 
            The opposite is true if the player's hand is closer to 21 than the dealer's, resulting in a win for the player.
            The player automatically loses if their hand exceeds a value of 21 during their turn (a bust).
            In the case of a tie ("push" or "standoff"), bets are returned without adjustment. A blackjack beats any hand that is not a blackjack, even one with a value of 21.

            If the player wins the hand, they recieve money at a ratio of 3:2 of their bet for that round as winnings.
            Upon a loss, the player loses the money that they have betted for that round.
            """)
        terminalin = input("---> ")
        start(terminalin)
    if terminalin == "start":
        return
    if terminalin != "start" and terminalin != "rules":
        print("Sorry, it looks like you haven't chosen \"start\" or \"rules\".")
        terminalin = input("---> ")
        start(terminalin)

def reset_game_vals():
    current_deck = [["Ace"], ["Ace"], ["Ace"], ["Ace"], ["One", 1], ["One", 1], ["One", 1], ["One", 1], ["Two", 2], ["Two", 2], ["Two", 2], ["Two", 2], ["Three", 3],
              ["Three", 3], ["Three", 3], ["Three", 3], ["Four", 4], ["Four", 4], ["Four", 4], ["Four", 4], ["Five", 5], ["Five", 5], ["Five", 5], ["Five", 5], ["Six", 6], ["Six", 6], ["Six", 6],
              ["Six", 6], ["Seven", 7], ["Seven", 7], ["Seven", 7], ["Seven", 7], ["Eight", 8], ["Eight", 8], ["Eight", 8], ["Eight", 8], ["Nine", 9], ["Nine", 9], ["Nine", 9], ["Nine", 9],
              ["Ten", 10], ["Ten", 10], ["Ten", 10], ["Ten", 10], ["Jack", 10], ["Jack", 10], ["Jack", 10], ["Jack", 10], ["Queen", 10], ["Queen", 10], ["Queen", 10], ["Queen", 10],
              ["King", 10], ["King", 10], ["King", 10], ["King", 10]]

    dealer_hand = []
    dealer_possible_values = []
    player_handone = []
    player_handtwo = []
    player_values_one = []
    player_values_two = []
    bet = 0
    total_cash = 500
    played_hands = 0
    return current_deck, dealer_hand, dealer_possible_values, player_handone, player_handtwo, player_values_one, player_values_two, bet, total_cash, played_hands

def reset_cash_and_number_of_games():
    bet = 0
    total_cash = 500
    played_hands = 0
    return bet, total_cash, played_hands

def start_game(total_cash, played_hands):
    print("Starting game...")
    print("Total Cash: $" , total_cash , " Played Hands: " , played_hands)
    print("How much money would you like to bet this round? (Type a number.)")
    bet = float(input("---> "))
    total_cash = total_cash - bet
    return bet, total_cash, played_hands
    
def dealerdraw(current_deck, dealer_hand, dealer_possible_values):
    dealer_drawn = current_deck.pop(random.randint(0, (len(current_deck) - 1)))
    dealer_hand.append(dealer_drawn[0])
    if len(dealer_possible_values) == 0:
        if dealer_drawn[0] == "Ace":
            dealer_possible_values.append(1)
            dealer_possible_values.append(11)
        else:
            dealer_possible_values.append(dealer_drawn[1])
    else:
        new_dealer_possible_values = []
        if dealer_drawn[0] == "Ace":
            for value in dealer_possible_values:
                new_dealer_possible_values.append(value + 1)
                new_dealer_possible_values.append(value + 11)
            dealer_possible_values = list(set(new_dealer_possible_values))
        else:
            for value in dealer_possible_values:
                new_dealer_possible_values.append(value + dealer_drawn[1])
            dealer_possible_values = new_dealer_possible_values
    return current_deck, dealer_hand, dealer_possible_values

def playerdraw(current_deck, player_hand, player_possible_values):
    player_drawn = current_deck.pop(random.randint(0,(len(current_deck) - 1)))
    player_hand.append(player_drawn[0])
    if len(player_possible_values) == 0:
        if player_drawn[0] == "Ace":
            player_possible_values.append(1)
            player_possible_values.append(11)
        else:
            player_possible_values.append(player_drawn[1])
    else:
        new_player_possible_values = []
        if player_drawn[0] == "Ace":
            for value in player_possible_values:
                new_player_possible_values.append(value + 1)
                new_player_possible_values.append(value + 11)
            player_possible_values = list(set(new_player_possible_values))
        else:
            for value in player_possible_values:
                new_player_possible_values.append(value + player_drawn[1])
            player_possible_values = new_player_possible_values
    return current_deck, player_hand, player_possible_values


def print_dealer_vals(dealer_hand, dealer_possible_values):
    if len(dealer_possible_values) == 1:
        if dealer_hand[-1] == "Eight":
            print("The dealer drew an Eight! (Total Hand Value:", dealer_possible_values[0] ,  ")")
        else:
            print("The dealer drew a", dealer_hand[-1], "! (Total Hand Value:", dealer_possible_values[0], ")")
    elif len(dealer_possible_values) == 2:
        if dealer_hand[-1] == "Ace":
            print("The dealer drew an Ace! (Possible Total Hand Values:", (dealer_possible_values[0]), "or", (dealer_possible_values[1]), ")")
        elif dealer_hand[-1] == "Eight":
            print("The dealer drew an Eight! (Possible Total Hand Values:", (dealer_possible_values[0]), "or", (dealer_possible_values[1]), ")")
        else:
            print("The dealer drew a", dealer_hand[-1], "! (Possible Total Hand Values:", (dealer_possible_values[0]), "or", (dealer_possible_values[1]), ")")
    elif len(dealer_possible_values) == 3:
        if dealer_hand[-1] == "Ace":
            print("The dealer drew an Ace! (Possible Total Hand Values:", (dealer_possible_values[0]), ",", (dealer_possible_values[1]), "or", (dealer_possible_values[2]), ")")
        elif dealer_hand[-1] == "Eight":
            print("The dealer drew an Eight! (Possible Total Hand Values:", (dealer_possible_values[0]), ",", (dealer_possible_values[1]), "or", (dealer_possible_values[2]), ")")
        else:
            print("The dealer drew a", dealer_hand[-1], "! (Possible Total Hand Values:", (dealer_possible_values[0]), ",", (dealer_possible_values[1]), "or", (dealer_possible_values[2]), ")")
    elif len(dealer_possible_values) == 4:
        if dealer_hand[-1] == "Ace":
            print("The dealer drew an Ace! (Possible Total Hand Values:", (dealer_possible_values[0]), ",", (dealer_possible_values[1]), ",", (dealer_possible_values[2]), "or", (dealer_possible_values[3]), ")")
        elif dealer_hand[-1] == "Eight":
            print("The dealer drew an Eight! (Possible Total Hand Values:", (dealer_possible_values[0]), ",", (dealer_possible_values[1]), ",", (dealer_possible_values[2]), "or", (dealer_possible_values[3]), ")")
        else:
            print("The dealer drew a", dealer_hand[-1], "! (Possible Total Hand Values:", (dealer_possible_values[0]), ",", (dealer_possible_values[1]), ",", (dealer_possible_values[2]), "or", (dealer_possible_values[3]), ")")

def print_player_vals(player_hand, player_possible_values):
    if len(player_possible_values) == 1:
        if player_hand[-1] == "Eight":
            print("The player was dealt an Eight! (Total Hand Value:", player_possible_values[0], ")")
        else:
            print("The player was dealt a", player_hand[-1], "! (Total Hand Value:", player_possible_values[0], ")")
    elif len(player_possible_values) == 2:
        if player_hand[-1] == "Ace":
            print("The player was dealt an Ace! (Possible Total Hand Values:", (player_possible_values[0]), "or", (player_possible_values[1]), ")")
        elif player_hand[-1] == "Eight":
            print("The player was dealt an Eight! (Possible Total Hand Values:", (player_possible_values[0]), "or", (player_possible_values[1]), ")")
        else:
            print("The player was dealt a", player_hand[-1], "! (Possible Total Hand Values:", (player_possible_values[0]), "or", (player_possible_values[1]), ")")
    elif len(player_possible_values) == 3:
        if player_hand[-1] == "Ace":
            print("The player was dealt an Ace! (Possible Total Hand Values:", (player_possible_values[0]), ",", (player_possible_values[1]), "or", (player_possible_values[2]), ")")
        elif player_hand[-1] == "Eight":
            print("The player was dealt an Eight! (Possible Total Hand Values:", (player_possible_values[0]), ",", (player_possible_values[1]), "or", (player_possible_values[2]), ")")
        else:
            print("The player was dealt a", player_hand[-1], "! (Possible Total Hand Values:", (player_possible_values[0]), ",", (player_possible_values[1]), "or", (player_possible_values[2]), ")")
    elif len(player_possible_values) == 4:
        if player_hand[-1] == "Ace":
            print("The player was dealt an Ace! (Possible Total Hand Values:", (player_possible_values[0]), ",", (player_possible_values[1]), ",", (player_possible_values[2]), "or", (player_possible_values[3]), ")")
        elif player_hand[-1] == "Eight":
            print("The player was dealt an Eight! (Possible Total Hand Values:", (player_possible_values[0]), ",", (player_possible_values[1]), ",", (player_possible_values[2]), "or", (player_possible_values[3]), ")")
        else:
            print("The player was dealt a ", player_hand[-1],"! (Possible Total Hand Values:", (player_possible_values[0]), ",", (player_possible_values[1]), ",", (player_possible_values[2]), " or ", (player_possible_values[3]), ")")

def check_if_blackjack(hand_values):
    if 21 in hand_values:
        return True
    else:
        return False
        
def draw(bet, total_cash, played_hands = 0):
    print("Hand Result: Draw. You will recoup your bet for this hand.")
    print("Total Cash = $" , total_cash , " + $" , bet , " = $" , (total_cash + bet))
    total_cash += bet
    return bet, total_cash, played_hands

def win(bet, total_cash, played_hands = 0):
    print("Hand Result: Win. You win money at a ratio of 3:2 based on your bet!")
    print("Total Cash = $" , total_cash , " + $" , (bet * (3/2)) , " = $" , (total_cash + (bet * (3/2))))
    total_cash += (bet * (3/2))
    return bet, total_cash, played_hands

def loss(bet, total_cash, played_hands = 0):
    print("Hand Result: Loss. You lose the money you bet on this hand.")
    print("Total Cash = $" , total_cash , ". You lost $" , bet , "as a bet.")
    return bet, total_cash, played_hands

def restart_query(cash_and_games):
    if cash_and_games[1] > 0.00:
        print("Would you like to play again? (Type y or n.)")
        terminalin = input("---> ")
        if terminalin == "y":
            new_game(cash_and_games)
        elif terminalin == "n":
            game_over()
        elif terminalin != "y" and terminalin != "n":
            print("Sorry, it looks like you haven't chosen \"y\" or \"n\".")
            terminalin = input("---> ")
            restart_query(terminalin)
    else:
        print("You're out of cash! Game over.")
        game_over(cash_and_games)

def initial_draws(next_game_vals, cash_and_games):
    print("Beginning the round. The dealer will draw one card.")
    dealer_vals = dealerdraw(next_game_vals[0], next_game_vals[1], next_game_vals[2])
    print_dealer_vals(dealer_vals[1], dealer_vals[2])
    print("Now the player will be dealt two cards.")
    player_vals = playerdraw(dealer_vals[0], next_game_vals[3], next_game_vals[5])
    print_player_vals(player_vals[1], player_vals[2])
    player_vals = playerdraw(player_vals[0], player_vals[1], player_vals[2])
    print_player_vals(player_vals[1], player_vals[2])
    deck = player_vals[0]
    if check_if_blackjack(player_vals[2]) == True:
        print("Lucky! You were dealt a blackjack! (Hand Value: 21)")
        if ("Ace" or "Jack" or "Queen" or "King") in dealer_vals[1]:
            print("The dealer can possibly draw a blackjack as well. Let's see if they do...")
            dealer_vals = dealerdraw(player_vals[0], dealer_vals[1], dealer_vals[2])
            print_dealer_vals(dealer_vals[1], dealer_vals[2])
            if check_if_blackjack(dealer_vals[2]) == True:
                print("The dealer got a blackjack too! This game is a draw.")
                cash_and_games = draw(cash_and_games[0], cash_and_games[1], cash_and_games[2])
                cash_and_games = list(cash_and_games)
                cash_and_games[2] += 1
                restart_query(cash_and_games)
            else:
                print("The dealer did not draw a blackjack! You win!")
                cash_and_games = win(cash_and_games[0], cash_and_games[1], cash_and_games[2])
                cash_and_games = list(cash_and_games)
                cash_and_games[2] += 1
                restart_query(cash_and_games)
        else:
            print("The dealer cannot possibly draw a blackjack! You win!")
            cash_and_games = win(cash_and_games[0], cash_and_games[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[2] += 1
            restart_query(cash_and_games)
    elif (player_vals[1][0] == player_vals[1][1]):
        split_answer = split_query(player_vals)
        if split_answer[0] == True:
            split_game(dealer_vals, split_answer[1], split_answer[2], split_answer[3], cash_and_games)
    else:
        normal_game(deck, dealer_vals, player_vals, cash_and_games)
      
def split_query(player_vals):
    print("You were dealt a pair! Would you like to split it and make two hands? (Type \"y\" or \"n\")")
    terminal_in = input("---> ")
    if terminal_in == "y":
        split_vals = split(player_vals)
        return split_vals
    elif terminal_in == "n":
        return False
    else:
        print("Sorry, it looks like you haven't chosen \"y\" or \"n\".")
        terminal_in = input("---> ")
        split_query(terminal_in)

def split(player_vals):
    player_hand_two = []
    player_values_two = []
    player_hand_two.append((player_vals[1].pop(-1)))
    player_values_two.append((player_vals[2].pop(-1)))
    return True, player_vals, player_hand_two, player_values_two

def split_game(dealer_vals, player_vals, player_hand_two, player_values_two, cash_and_games):
    print("How much would you like to bet on your second hand? Your previous bet will remain on your first hand. (Type a plain number.)")
    print("Total Cash: $",cash_and_games[1])
    bet_two = int(input("---> "))
    if bet_two > cash_and_games[1]:
        print("You don't have enough money to bet that much!")
        split_game(dealer_vals, player_vals, player_hand_two, player_values_two, cash_and_games)
    cash_and_games = list(cash_and_games)
    cash_and_games[1] -= bet_two
    print("You split your hand into two. Each hand will now be dealt a card.")
    print("First Hand:")
    first_hand_vals = playerdraw(player_vals[0], player_vals[1], player_vals[2])
    deck = first_hand_vals[0]
    print_player_vals(first_hand_vals[1], first_hand_vals[2])
    print("Second Hand:")
    second_hand_vals = playerdraw(deck, player_hand_two, player_values_two)
    deck = second_hand_vals[0]
    print_player_vals(second_hand_vals[1], second_hand_vals[2])
    print("It's time to play for your first hand. (Type \"hit\" or \"stand\".)")
    print("Total Cash: $", cash_and_games[1])
    hand_one_score = player_turn(deck, first_hand_vals, cash_and_games[0], cash_and_games[1], False)
    deck = hand_one_score[-1]
    current_cash = [hand_one_score[2], hand_one_score[3]]
    if hand_one_score[0] == False:
       current_cash = loss(current_cash[0], current_cash[1], cash_and_games[2])
       cash_and_games[1] = current_cash[1]
       cash_and_games[2] += 1
    print("It's time to play for your second hand. (Type \"hit\" or \"stand\".)")
    print("Total Cash: $"+ hand_one_score[3])
    hand_two_score = player_turn(deck, second_hand_vals, bet_two, hand_one_score[3], False)
    deck = hand_two_score[-1]
    current_cash = [bet_two, current_cash[1]]
    if hand_two_score[0] == False:
        current_cash = loss(current_cash[0], current_cash[1], cash_and_games[2])
        cash_and_games[1] = current_cash[1]
        cash_and_games[2] += 1
    if hand_one_score[0] and hand_two_score[0] == False:
        print("Both of your hands busted! This round is over.")
        restart_query(cash_and_games)
    print("It's time for the dealer to resolve their hand...")
    dealer_score = dealer_resolve(deck, dealer_vals)
    if dealer_score == False:
        if hand_one_score[0] and hand_two_score[0] != False:
            print("Both of your hands win!")
            print("Hand One:")
            current_cash = win(hand_one_score[2], current_cash[1], cash_and_games[2])
            print("Hand Two:")
            current_cash = win(bet_two, current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
            restart_query(cash_and_games)
        elif (hand_one_score[0] != False):
            print("Hand One wins!")
            current_cash = win(hand_one_score[2], current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
            restart_query(cash_and_games)
        elif (hand_two_score[0] != False):
            print("Hand Two wins!")
            current_cash = win(bet_two, current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
            restart_query(cash_and_games)
    else:
        if (hand_one_score[0] != False) and (hand_one_score[0] > dealer_score):
            print("Hand One wins! (Hand One Score = ",hand_one_score[0]," > Dealer's Score = ",dealer_score,")") 
            current_cash = win(hand_one_score[2], current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
        if (hand_one_score[0] != False) and (hand_one_score[0] < dealer_score):
            print("Hand One loses... (Hand One Score = ",hand_one_score[0]," > Dealer's Score = ",dealer_score,")")
            current_cash = loss(hand_one_score[2], current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
        if (hand_one_score[0] != False) and (hand_one_score[0] == dealer_score):
            print("Hand One draws! (Hand One Score = ", hand_one_score[0], " == Dealer's Score = ",dealer_score,")")
            current_cash = draw(hand_one_score[2], current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
        if (hand_two_score[0] != False) and (hand_one_score[0] > dealer_score):
            print("Hand Two wins! (Hand Two Score = ",hand_two_score[0]," > Dealer's Score = ",dealer_score,")")
            current_cash = win(hand_two_score[2], current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
        if (hand_two_score[0] != False) and (hand_two_score[0] < dealer_score):
            print("Hand Two loses... (Hand Two Score = ",hand_two_score[0]," > Dealer's Score = ",dealer_score,")")
            current_cash = loss(hand_two_score[2], current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
        if (hand_two_score[0] != False) and (hand_one_score[0] == dealer_score):
            print("Hand Two draws! (Hand One Score = ", hand_one_score[0], " == Dealer's Score = ",dealer_score,")")
            current_cash = draw(hand_two_score[2], current_cash[1], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
        restart_query(cash_and_games)
        
def normal_game(deck, dealer_vals, player_vals, cash_and_games):
    print("It's time to play your hand. (Type \"hit\", \"stand\", or \"double\".)")
    print("Total Cash: $",  cash_and_games[1])
    hand_vals = []
    hand_vals = player_turn(deck, player_vals, cash_and_games[0], cash_and_games[1], True)
    if hand_vals[0] == False:
            current_cash = loss(hand_vals[1], hand_vals[2], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
            restart_query(cash_and_games)
    print("It's time for the dealer to resolve their hand...")
    dealer_score = dealer_resolve(deck, dealer_vals)
    if dealer_score == False:
        print("Your hand wins!")
        current_cash = win(hand_vals[1], hand_vals[2], cash_and_games[2])
        cash_and_games = list(cash_and_games)
        cash_and_games[1] = current_cash[1]
        cash_and_games[2] += 1
    else:
        if hand_vals[0] > dealer_score:
            print("Your hand wins! (Your Score = ", hand_vals[0], " > Dealer's Score = ", dealer_score, ")")
            current_cash = win(hand_vals[1], hand_vals[2], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
        elif hand_vals[0] == dealer_score:
            print("It's a draw! (Your Score = ", hand_vals[0], " == Dealer's Score = ", dealer_score, ")")
            current_cash = draw(hand_vals[1], hand_vals[2], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
        else:
            print("Your hand loses... (Your Score = ", hand_vals[0], " < Dealer's Score = ",dealer_score, ")")
            current_cash = loss(hand_vals[1], hand_vals[2], cash_and_games[2])
            cash_and_games = list(cash_and_games)
            cash_and_games[1] = current_cash[1]
            cash_and_games[2] += 1
    restart_query(cash_and_games)

def player_turn(deck, player_hand_vals, bet, total_cash, double_possible = True):
    choice = input("---> ")
    if choice == "hit":
        print("You chose to hit!")
        double_possible = False
        player_hand_vals = playerdraw(deck, player_hand_vals[1], player_hand_vals[2])
        print_player_vals(player_hand_vals[1], player_hand_vals[2])
        if min(player_hand_vals[2]) > 21:
            print("Unfortunately... You busted. (All possible hand scores are greater than 21).")
            return False, bet, total_cash
        print("What action would you like to take next? (Type \"hit\" or \"stand\".)")
        return player_turn(deck, player_hand_vals, bet, total_cash, double_possible)
    elif choice == "stand":
        hand_score = max([i for i in player_hand_vals[2] if i <= 21])
        print("You've chosen to stand. The best score for this hand is", hand_score, ".")
        return hand_score, bet, total_cash, deck
    elif choice == "double":
        if double_possible:
            if bet > total_cash:
                print("You don't have enough money to double down on this hand! (Current Bet on This Hand: $",bet,", Total Cash: $",total_cash,")")
                print("What action would you like to take next? (Type \"hit\" or \"stand\".)")
            else:
                total_cash -= bet
                bet *= 2
                print("You chose to double down on this hand! Good luck! (Current Bet on This Hand: $",bet,", Total Cash: $",total_cash,")")
                player_hand_vals = playerdraw(deck, player_hand_vals[1], player_hand_vals[2])
                print_player_vals(player_hand_vals[1], player_hand_vals[2])
                if min(player_hand_vals[2]) > 21:
                    print("You've gone and busted my good man... (All possible hand scores are greater than 21).")
                    return False, bet, total_cash
                hand_score = max([i for i in player_hand_vals[2] if i <= 21])
                print("The best score for this hand is ", hand_score, ".")
                return hand_score, bet, total_cash, deck
        else:
            print("You can't double down after hitting or splitting!")
            print("What action would you like to take next? (Type \"hit\" or \"stand\".)")
            return player_turn(deck, player_hand_vals, bet, total_cash, False)
    else:
        print("Sorry, it looks like you haven't chosen a valid action. (Type \"hit\", \"stand\", or \"double\" if available.)")
        player_turn(deck, player_hand_vals, bet, total_cash, double_possible)

def dealer_resolve(deck, hand_vals):
    while (int(min(hand_vals[2]))) < 17:
        hand_vals = dealerdraw(deck, hand_vals[1], hand_vals[2])
        print_dealer_vals(hand_vals[1], hand_vals[2])
    if (int(min(hand_vals[2]))) > 21:
        print("The dealer has busted! (All possible hand scores are greater than 21).")
        return False
    else:
        dealer_score = max([i for i in hand_vals[2] if i <= 21])
        return dealer_score

def new_game(cash_and_games):
    next_game_vals = reset_game_vals()
    cash_and_games  = start_game(cash_and_games[1], cash_and_games[2])
    initial_draws(next_game_vals, cash_and_games)

def game_over():
    print("Game over! Returning to title.")
    blackjack()

def blackjack():
    title()
    terminal_in = input("---> ")
    start(terminal_in)
    cash_and_games = reset_cash_and_number_of_games()
    new_game(cash_and_games)

blackjack()