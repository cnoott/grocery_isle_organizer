isleList = [["ice_cream","pizza"],["veg","rice"]]
#input list
inputList = []
numList = int(input("How many items do you have in your list?"))
for n in range(numList):
    items = input("Enter item")
    inputList.append(items)
print(inputList)
