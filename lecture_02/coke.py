def main():
    cokeCost = 50
    amountDue = cokeCost;
    acceptedCoins = {25, 10, 5}

    while amountDue > 0:
        print("Amount due:", amountDue)
        insertedCoin = int(input("Insert coin: "))
        if (insertedCoin in acceptedCoins):
            amountDue -= insertedCoin

    if amountDue < 0:
        amountDue = amountDue * -1

    print("Change owed:", amountDue)

main()