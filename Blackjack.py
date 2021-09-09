import random

user_cards = []
dealer_cards = []

def startGame():
    user_cards.append(random.randint(1,11))
    user_cards.append(random.randint(1,11))

    dealer_cards.append(random.randint(1,11))
    dealer_cards.append(random.randint(1,11))

    print("The dealer has cards X, " + str(dealer_cards[1]))

    while sum(dealer_cards) < 22:
        if sum(dealer_cards) < 17:
            print("The dealer has decided to twist.")
            dealer_cards.append(random.randint(1,11)) 

            if sum(dealer_cards) >=22:
                print("The dealer has gone bust with " + str(sum(dealer_cards)) + "! You win!")
                quit()
        else:
            print("The dealer has decided to stick.")
            break

    print("Your cards are " + str(user_cards))
    while sum(user_cards) < 22: 

        user_decision = input("Do you wish to stick or twist? ")
        if user_decision == "stick":
            break
        elif user_decision == "twist":
            user_cards.append(random.randint(1,11))
            print("Your cards are " + str(user_cards) )
        else:
         print("This is not a valid option.")

    if sum(user_cards) >= 22:
        print("Your total is " + str(sum(user_cards)) + ". You are bust!")

    

    elif sum(user_cards) <22 and sum(user_cards) > sum(dealer_cards):
        print("Your total is " + str(sum(user_cards)) + ". The dealer's total is " + str(sum(dealer_cards)) + ". You win!")

    elif sum(dealer_cards) <22 and sum(dealer_cards) > sum(user_cards):
        print("Your total is " + str(sum(user_cards)) + ". The dealer's total is " + str(sum(dealer_cards)) + ". You lose!")

    elif sum(user_cards) ==  sum(dealer_cards):
        print("It's a tie! Everyone loses!")

    else:
        print("The dealer's total is " + str(sum(dealer_cards)))
        print("Your total is " + str(sum(user_cards)))

startGame()