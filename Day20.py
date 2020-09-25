# Day 20 - 
import math

# presentsToFind = 500
presentsToFind = 33100000

# house=list()
# houseNumbers = list(range(1, maxNumOfHouses+1))

def Part1():
    # Let's start at a reasonable high number house
    house = 100000
    maxHouse = 800000
    presents = 0

    #Continue to check until the number of presents is => the number of presents to find
    while (presents < presentsToFind) and (house < maxHouse):

        # Find the elves that visit any house by creating a list of elf numbers where house is an even divisor of House #
        # elvesThatVisit = [x for x in range(1, (house // 2) + 1) if house % x == 0]
        elvesThatVisit=[1]
        i = 2
        while i <= math.sqrt(house):
            if (house % i) == 0:
                if (house / i == i):
                    elvesThatVisit.append(i)
                else:
                    elvesThatVisit.append(i)
                    elvesThatVisit.append(house // i)
            i += 1


        # Append the house number as the last in the range
        elvesThatVisit.append(house)

        # Sum the number of presents, which is equal to 10 times the number of each elf that visits
        presents = sum(elvesThatVisit)*10

        # print(f"House: {house} - {elvesThatVisit} - Presents {presents}")
        # print(f"House: {house} - elves {elvesThatVisit} - Presents {presents}")
        if presents > 30000000:
            print(f"House: {house} - elves {len(elvesThatVisit)} - Presents {presents}")
        if (house % 1000 == 0):
            print(house)
        house += 1
    
    # Print the final result
    print(f"House: {house} - elves {len(elvesThatVisit)} - Presents {presents}")

Part1()
