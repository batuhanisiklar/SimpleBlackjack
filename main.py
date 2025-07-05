from art import logo
import random

# -----------------------------------------------------#
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# -----------------------------------------------------#
def player_cards():
    player_score = 0
    numbers = []
    for i in range(2):
        number = random.choice(cards)
        numbers += [number]
    return (numbers)
# -----------------------------------------------------#
def player_card_total(cards):
    total = 0
    for i in range(2):
        total += cards[i]
    return total
# -----------------------------------------------------#
def new_cards():
    number = random.choice(cards)
    return (number)
# -----------------------------------------------------#
def who_win(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# -----------------------------------------------------#
def finish():
    print(logo)
    cnt = 0
    computer_total = new_cards()
    player_card = player_cards()
    player_total = player_card_total(player_card)
    computer_card = [computer_total]
    new_computer_card = computer_card
    new_computer_total = computer_total
    print("Your cards:", player_card, "Current score:", player_total)
    print("Computer's first card:", computer_card[0])
    # ------------------------------------------------------#
    while new_computer_total < 17:
        new_card = new_cards()
        new_computer_card += [new_card]
        new_computer_total += new_card
        if new_computer_total > 21:
            for i in range(len(new_computer_card)):
                if new_computer_card[i] == 11:
                    new_computer_card[i] = 1
                    new_computer_total -= 10
    if player_total == 21 and len(player_card) == 2:
        print("Your cards:", player_card, "Final score:", player_total)
        print("Computer's final hand:", new_computer_card, "Final score:",
              new_computer_total)
        print(who_win(0, new_computer_total))
        print("#---------------------------------------------------------------#")
    elif new_computer_total == 21 and len(new_computer_card) == 2:
        print("Your cards:", player_card, "Final score:", player_total)
        print("Computer's final hand:", new_computer_card, "Final score:",
              new_computer_total)
        print(who_win(player_total, 0))
        print("#---------------------------------------------------------------#")


    # ----------------------------------------------------------------------------------------------------------#
    else:
        for i in range(5):
            ques = input("Type 'y' to get another card, type 'n' to pass:")
            if ques == "y":
                new_number = new_cards()
                player_card += [new_number]
                player_total += new_number
                if player_total > 21:
                    for i in range(len(player_card)):
                        if player_card[i] == 11:
                            player_card[i] = 1
                            player_total -= 10
                if player_total < 22:
                    print("Your cards:", player_card, "Current score:", player_total)
                    print("Computer's first card:", computer_card[0])
                    print(
                        "#---------------------------------------------------------------#"
                    )
                else:
                    print("Your cards:", player_card, "Final score:", player_total)
                    print("Computer's final hand:", new_computer_card, "Final score:",
                          new_computer_total)
                    print(who_win(player_total, new_computer_total))
                    print(
                        "#---------------------------------------------------------------#"
                    )
                    break
            elif ques == "n":
                print("Your cards:", player_card, "Final score:", player_total)
                print("Computer's final hand:", new_computer_card, "Final score:",
                      new_computer_total)
                print(who_win(player_total, new_computer_total))
                print(
                    "#---------------------------------------------------------------#")
                break
            else:
                print("You entered incorrectly")
                break
    # ----------------------------------------------------------------------------------------------------------#
    question2 = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if question2 == "y":
        finish()
    # ----------------------------------------------------------------------------------------------------------#


question = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if question == "y":
    finish()
else:
    print("Bye!!")