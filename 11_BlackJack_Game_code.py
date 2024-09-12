import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
Black_Jack = True


def winner(player_total, dealer_total, player_cards, dealer_cards):
    if player_total == 21 and dealer_total != 21:
        print(f"It's a \"Black Jack\": {player_cards}, final score: {player_total}")
        print(f"Computer final hand: {dealer_cards}, final score: {dealer_total}")
        print("You WIN..!!😎")
    elif dealer_total == 21 and player_total != 21:
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"It's a \"Black Jack\" for Computer: {dealer_cards}, final score: {dealer_total}")
        print("You Loose..!!😭")
    elif player_total > dealer_total and player_total <= 21:
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"Computer final hand: {dealer_cards}, final score: {dealer_total}")
        print("You WIN..!!😎")
    elif player_total > dealer_total and player_total > 21:
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"Computer final hand: {dealer_cards}, final score: {dealer_total}")
        print("You Loose..!!😭")
    elif player_total < dealer_total and dealer_total <= 21:
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"Computer final hand: {dealer_cards}, final score: {dealer_total}")
        print("You Loose..!!😭")
    elif player_total == dealer_total:
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"Computer final hand: {dealer_cards}, final score: {dealer_total}")
        print("Its a Draw..!!")
    elif player_total < dealer_total and dealer_total > 21:
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"Computer final hand: {dealer_cards}, final score: {dealer_total}")
        print("You WIN..!!😎")


while Black_Jack:
    play_cards = []
    play_total = 0
    deal_cards = []
    deal_total = 0
    dummy_play = []
    dummy_deal = []
    hit = True
    next_round = True
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        #print("\n" * 20, art.logo)
        print("\n" * 20, logo)
        # TODO: PLAYER CARDS SELECTION
        for i in range(0, 2):
            play_cards.append(random.choice(cards))
        play_total = sum(play_cards)
        dummy_play.append(play_cards[1])
        if play_total == 22 and dummy_play[0] == 11:
            play_cards[1] = 1
        play_total = sum(play_cards)
        print(f"Your Cards: {play_cards}, Current Score: {play_total}")

        # TODO: DEALER CARDS SELECTION
        for j in range(0, 2):
            deal_cards.append(random.choice(cards))
        deal_total = sum(deal_cards)
        dummy_deal.append(deal_cards[1])
        if deal_total == 22 and dummy_deal[0] == 11:
            deal_cards[1] = 1
        deal_total = sum(deal_cards)
        print(f"Computer's first card: {deal_cards[0]}, {deal_cards}")
    else:
        print("Good Bye..!")
        Black_Jack = False
        hit = False

    while hit:
        if play_total == 21 or deal_total == 21:
            winner(play_total, deal_total, play_cards, deal_cards)
            hit = False
            next_round = False
        while next_round:
            hit_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            # TODO: PLAYER CHOOSING ONE MORE CARD
            if hit_pass == 'y':
                play_cards.append(random.choice(cards))
                play_total = sum(play_cards)
            # TODO: TO CHECK IF PLAYER HAS GOT AN ACE (11) and CONVERTING IT TO 1 IF TOTAL IS < 21
                if play_total > 21 and max(play_cards) == 11:
                    element = -1
                    for k in play_cards:
                        element += 1
                        if k == 11:
                            play_cards[element] = 1
                            break
                play_total = sum(play_cards)
                print(f"Your Cards: {play_cards}, Current Score: {play_total}")
                print(f"Computer's first card: {deal_cards[0]}")
                if play_total >= 21:
                    hit = False
                    next_round = False
                    winner(play_total, deal_total, play_cards, deal_cards)

            # TODO: PLAYER CHOOSING TO STAY
            elif hit_pass == 'n':
                while deal_total <= 16:
                    deal_cards.append(random.choice(cards))
                    deal_total = sum(deal_cards)
                    # TODO: CHECK
                    if deal_total > 21 and max(deal_cards) == 11:
                        element = -1
                        for n in deal_cards:
                            element += 1
                            if n == 11:
                                deal_cards[element] = 1
                                break
                    deal_total = sum(deal_cards)

                hit = False
                next_round = False
                winner(play_total, deal_total, play_cards, deal_cards)


