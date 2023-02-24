def findBlackjackScore(hand):
    ranks = []
    suits = []
    values = []
    value = 0
    total = 0

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
            if rank == "A" or rank == "J" or rank == "Q" or rank == "K":
                value = 10
            else:
                value = int(rank)

        else:
            rank = card[0:2]
            suit = card[2]
            if rank == "A" or rank == "J" or rank == "Q" or rank == "K":
                value = 10
            else:
                value = int(rank)

        values.append(value)

    #print(values)

    for value in values:
        total = total + value

    #print(total)

    return total






if __name__ =='__main__':

    values = findBlackjackScore(["8h", "2c", "7c", "Ah"])

