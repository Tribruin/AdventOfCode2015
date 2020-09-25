# Day 20 - 

maxNumOfHouses = 20
presentsToFind = 33100000

# house=list()
# houseNumbers = list(range(1, maxNumOfHouses+1))

def Part1():
    # Let's start at a reasonable high number house
    house = 700000
    presents = 0

    #Continue to check until the number of presents is => the number of presents to find
    while presents < presentsToFind:

        # Find the elves that visit any house by creating a list of elf numbers where house is an even divisor of House #
        elvesThatVisit = [x for x in range(1, house+1) if house % x == 0]

        # Sum the number of presents, which is equal to 10 times the number of each elf that visits
        presents = sum([x * 10 for x in elvesThatVisit])

        # print(f"House: {house} - {elvesThatVisit} - Presents {presents}")
        print(f"House: {house} - elves {len(elvesThatVisit)} - Presents {presents}")
        house += 1
    
    # Print the final result
    print(f"House: {house} - elves {len(elvesThatVisit)} - Presents {presents}")

Part1()
