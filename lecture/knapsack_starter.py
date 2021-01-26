'''Explorer's Dilemna - aka the Knapsack Problem
After spending several days exploring a deserted island out in the Pacific, 
you stumble upon a cave full of pirate loot! There are coins, jewels, 
paintings, and many other types of valuable objects.

However, as you begin to explore the cave and take stock of what you've 
found, you hear something. Turning to look, the cave has started to flood! 
You'll need to get to higher ground ASAP. 

There IS enough time for you to fill your backpack with some of the items 
in the cave. Given that...
- you have 60 seconds until the cave is underwater
- your backpack can hold up to 50 pounds
- you want to maximize the value of the items you retrieve (since you can 
only make one trip)

HOW DO YOU DECIDE WHICH ITEMS TO TAKE?
'''
import random
import time
from itertools import combinations


# Artem 07.13.20

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.efficiency = 0

    def __str__(self):
        return f'{self.name}, {self.weight} lbs, ${self.value}'


def naive_fill_knapsack(sack, items):
    '''# Put highest value items in knapsack until full
    (other basic, naive approaches exist)
    '''
    # TODO - sort items by value
    items.sort(key=lambda x: x.value, reverse=True)

    # TODO - put most valuable items in knapsack until full
    weight = 0
    for item in items:
        weight += item.weight
        if weight > 50:
            return sack
        else:
            sack.append(item)
    return sack


def brute_force_fill_knapsack(sack, items):
    ''' Try every combination to find the best'''

    # TODO - generate all possible combinations of items
    combos = []

    # TODO - calculate the value of all combinations
    for i in range(1, len(items) + 1):
        list_of_combos = list(combinations(items, i))
        for combo in list_of_combos:
            combos.append(list(combo))

    best_value = -1
    # for each combo, add up all the wieght and value of the items, and save the best one
    # find the combo with the highest value
    for combo in combos:
        value = 0
        weight = 0
        for item in combo:
            value += item.value
            weight += item.weight
        if weight <= 50 and value > best_value:
            best_value = value
            # this is the combo thats far the best we have seen, set the backpack to this combo
    return sack


def greedy_fill_knapsack(sack, items):
    '''Use ratio of [value] / [weight] 
    to choose items for knapsack
    '''

    # TODO - calculate efficiencies
    # golden ratio
    for item in items:
        item.efficiency = item.value / item.weight

    # TODO - sort items by efficiency
    items.sort(key=lambda x: x.efficiency, reverse=True)

    # TODO - put items in knapsack until full
    weight = 0
    for item in items:
        weight += item.weight
        if weight > 50:
            return sack
        else:
            sack.append(item)
    return sack


# TESTS -
# Below are a series of tests that can be utilized to demonstrate
# the differences between each approach. Timing is included to give
# students an idea of how poorly some approaches scale. However,
# efficiency should also be formalized using Big O notation.

small_cave = []
medium_cave = []
large_cave = []


def fill_cave_with_items():
    '''Randomly generates Item objects and 
    creates caves of different sizes for testing
    '''
    names = ["painting", "jewel", "coin", "statue", "treasure chest",
             "gold", "silver", "sword", "goblet", "hat"]

    for _ in range(5):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        small_cave.append(Item(n, w, v))

    for _ in range(15):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        medium_cave.append(Item(n, w, v))

    for _ in range(25):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        large_cave.append(Item(n, w, v))


def print_results(items, knapsack):
    '''Print out contents of what the algorithm  
    calculated should be added to the knapsack
    '''
    # print(f'\nItems in the cave:')
    # for i in items:
    #     print(i)

    print('\nBest items to put in knapsack: ')
    for item in knapsack:
        print(f'-{item}')
    print(f'\nResult calculated in {time.time()-start:.5f} seconds\n')

    print('\n-------------------------')


fill_cave_with_items()
knapsack = []

# Test 1 - Naive
print('\nStarting test 1, naive approach...')
items = large_cave
start = time.time()
knapsack = naive_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# # Test 2 - Brute Force
print('Starting test 2, brute force...')
items = medium_cave
start = time.time()
knapsack = brute_force_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# Test 3 - Brute Force
# print('Starting test 3, brute force...')
# items = large_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print_results(items, knapsack)

# # Test 4 - Greedy
# print('Starting test 4, greedy approach...')
# items = medium_cave
# start = time.time()
# greedy_fill_knapsack(knapsack, items)
# print_results(items, knapsack)

knapsack = []
# Test 5 - Greedy
print('Starting test 5, greedy approach...')
items = large_cave
start = time.time()
greedy_fill_knapsack(knapsack, items)
print_results(items, knapsack)


'''
NOTES:
First Pass Solution:
    - not worrying about performance
    - No big O
Start with the Naive approach
    - 

Brute Force:
    - What will it look like?
        - 

Greedy:
    - What metric is best?
    - efficiency
    - value / weight  
        
'''
