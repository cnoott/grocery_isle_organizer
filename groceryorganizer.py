#Created by Liam Amadio
#November 28, 2019
#This program takes a shopping list as input and sorts the items based on what isle they are in

isle_items = {"banana":1, "apple":1,"pizza":2,"peas":2,"rice":3}
shopping_list = ["banana", "pizza", "peas", "apple", "rice"]

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
