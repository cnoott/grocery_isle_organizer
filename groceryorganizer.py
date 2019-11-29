#Created by Liam Amadio
#November 28, 2019
#This program takes a shopping list as input and sorts the items based on what isle they are in

isle_items = {"banana":1, "apple":1,"pizza":2,"peas":2,"rice":3}
shopping_list = ["banana", "pizza", "peas", "apple", "rice"]

#print("Isle 1 \n-----")
#for i in shopping_list:
#    if isle_items[i] == 1:
#        print(i)
#print("Isle 2 \n-----")
#for i in shopping_list:
#    if isle_items[i] == 2:
#        print(i)
#print("Isle 3 \n-----")
#for i in shopping_list:
#    if isle_items[i] == 3:
#        print(i)


x = 1
for i in range(len(shopping_list)):
    print("Isle",i + 1)
    for i in shopping_list:
        if isle_items[i] == x:
            print(i)
        x = x + 1

