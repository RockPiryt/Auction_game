#Auction program
import os

print('Welcome in paint auction')
print('We start biding. Please make your bids.')


#empty dict for bids from user
player_bids = {}

def higest_bid(bids):
    """function find the highest value of bid from player"""

    #Example: bids = {'Tom':12, 'Paweł':15, 'Paulina':20}

    highest_value = 0 #entry value beyond for loop
    winner = ' '#entry value beyond for loop

    #iterate for player_bids:
    for player in bids:# player is key in bids_dict
        player_bid = bids[player]#value of each bids from all players

        #highest_value = 0 #nie tutaj bo bede porównywać kolejny zakład zawsze do 0
        #winner = ' '#nie tutaj bo winnerem będzie każdy kolejny player bo porównane do zera

        #if (paweł_bid)15> 0:
            #winner to paweł

        if player_bid > highest_value:
            highest_value = player_bid #assign highest player_bid  to  variable higest_value
            winner = player

    print(f'The winner is {winner} with a bid of ${highest_value}')





#conditional for while loop to start
biding = True

#Start auction - while loop
while biding is True:
    name = input('Please give me your name: ')
    price = int(input('Plese give me your price for paint: $ '))
    #Add bid to dict
    player_bids[name] = price
    count_players = len(player_bids)
    print(f'In auction we have {count_players} players: ')
    for player in player_bids:
        print(player)
    another_player_question = input('Is there another player? Type "y" for yes or "n" for no other players: ')

    if another_player_question == 'y':
        os.system('cls')# clear window in terminal
        bids=player_bids #change name, if not to def it going empty dict player_bids from up
        higest_bid(bids) #call function to choose highest bid from all players
    else:
        print('We end entering new players')
        #end loop
        biding = False
