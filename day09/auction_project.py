# Secret Auction
# --------------------------------------------- #

auction_entry = {}
next = True
print("Welcome to the secret auction program.")

def find_highest(bidding_dict):
    # winner = ""
    # highest_bid = 0

    highest_bid = max(bidding_dict, key=bidding_dict.get)


    # for key in bidding_dict:
    #     bid_amount = bidding_dict[key]
    #     if bid_amount > highest_bid:
    #         highest_bid = bid_amount 
    #         winner = key

    print(f"The winner is {highest_bid} with a bid of ${bidding_dict[highest_bid]}.")

while next:
    key = input("What is your name?: ")
    value = int(input("What is you bid?: $"))

    auction_entry[key] = value

    others = input("Are there any other bidders? type 'yes' or 'no': ").lower()

    if others == 'yes':
        print("\n" * 100)
        next = True
    elif others == 'no':
        next = False
        find_highest(auction_entry)
    else:
        print("Error")
    



# print(auction_entry)