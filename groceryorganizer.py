#Created by Liam Amadio
#November 28, 2019
#This program takes a shopping list as input and sorts the items based on what isle they are in
from isle_items import isle_items
shopping_list = ["cold beer", "club soda", "wheat bread", "rice", "merlot wine", "penut butter and jelly", "spicy sauce", "fish"]
#inventory = {'beer':1, 'soda':1, 'bread':2, 'rice':2, 'pickles':3, 'honey':3}
inventory = isle_items
for isle in range(1,3):
    print("Isle",isle,"\n-----")
    for key in inventory:
        for item in shopping_list:
            if key in item and inventory[key] == isle:
                print(item)


