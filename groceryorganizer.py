#Created by Liam Amadio
#November 28, 2019
#This program takes a shopping list as input and sorts the items based on what isle they are in
from isle_items import isle_items
shopping_list = ["beer", "club soda", "bread", "rice", "vegetables", "pickles", "honey"]

x = 1
for j in range(len(shopping_list)):
    for i in shopping_list:
        if isle_items[i] == x:
            print("Isle", x,"\n-----")
            break
    for i in shopping_list:
        if isle_items[i] == x:
            print(i)
    x = x + 1
