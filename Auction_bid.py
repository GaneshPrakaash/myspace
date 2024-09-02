import art
print(art.logo)
print("Welcome to the Secret Auction Program..!")
# bidding = {}
# bidding = {
#    "bidder_name" : ["name1", "name2", "name3", "name4"],
#    "bid_amt" : ["$1", "$2", "$3", "$4"],
#    "bid_no" : [0, 1, 2, 3]
# }
# bidding = {
#    "user_1" : 23,
#    "user_2" : 27,
#    "user_3" : 24,
# }

count = 0
proceed = True
bidding = {}


def bidder(bid_win):
    winner = ""
    bid_dollar = 0
    for user in bidding:
        if int(bidding[user]) > bid_dollar:
            bid_dollar = int(bidding[user])
            winner = user
    print("\n" * 20)
    print(f"The Winner of the Bidding is {winner} by bidding ${bid_dollar}")

    game_on = ""


while proceed:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bidding[name] = bid
    pro = input("Are there any other Bidder? Type 'yes' or 'no' \n")
    if pro == "no":
        proceed = False
        bidder(bidding)
    elif pro == "yes":
        print("\n" * 20)


