############################################################################################################################
############################################################################################################################
#THIS FUNCTION IS USED FIR THE GAME LOGIC
############################################################################################################################


#Define function
def findBlackjackScore(hand):
    
    ranks = []
    suits = []
    values = []
    value = 0
    total = 0

    #Get a list from main and iterate over every value
    for card in hand:
        #If the card value is = 2 charachters EX "9h" (9 of hearts)
        if len(card) == 2:
            #Then the rank is equal to the value on index 0 (Ex: 9) since 9 is on index 0
            rank = card[0]
            #The suit is the item on index 1 (Ex: h) since h is on index 1 
            suit = card[1]
            #Check if the rank equals a face card, if it does then change the value to 10
            if rank == "A" or rank == "J" or rank == "Q" or rank == "K":
                value = 10
            #If the card is a number card, then the value is equal to the rank
            else:
                value = int(rank)

        else:
            #This condition is used if the len of card is greater than 2 (Ex: 10c) 10 of clubs
            # If it is then we grab the items on indexes 0 and 1 (Ex 10)
            rank = card[0:2]
            #here the suit is the item on idex 2 (Ex c)
            suit = card[2]
            if rank == "A" or rank == "J" or rank == "Q" or rank == "K":
                value = 10
            else:
                value = int(rank)
        
        #Once we get the values from the array we appan them to the "values" list
        values.append(value)

    #print(values)
    
    #Here we iterate through the items in the values array and we add them up
    for value in values:
        total = total + value

    #print(total)
    
    #return the total
    return total






if __name__ =='__main__':

    values = findBlackjackScore(["8h", "2c", "7c", "Ah"])

