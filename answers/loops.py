

# Done all following questions to have $10

#1. Write a Python function to reverse the order of the items from an array
# array1 = [1, 2, 3, 4, 5, 6, 7]
# def flipArray(array):
   

# #reverses the order of the array using list slicing
#     flip = array [::-1]
# #prints the reversed array
#     return (flip)

# print(flipArray(array1))

#2. Write a Python function to sort an array by ascending or descending

# array = [13, 24, 366, 1, 2,]
# def arrayDA(array, isAscending= True):
#     # sorts array least to greatest
#     array.sort(reverse = not(isAscending))
#     return array

# print("Numbers acending are:")
# print(arrayDA(array, True))

# print("Numbers desending are:")
# print(arrayDA(array, False))

#3. Write a Python function to return the appearance of a specified element in an array
#imports methods and variables so you do not need to prefix them
# array1 = [1, 3, 5, 3, 7, 3]
# rem = 5
# def occArr(arrayNum, remNum):
    
#     result = arrayNum.count(remNum)
#     return result

# #counts and prints the occurences of 3

# print(f"Number of occurences of number {rem}: {occArr(array1, rem)}")

#4. Write a Python function to sort a dictionary on value
# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}


# THIS WON'T WORK

# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}

# def valueDict(dictionary, reverse= False):
#     sortedDict = {}
#     sortedKey = sorted(dictionary, key=dictionary.get, reverse= reverse)

#     for w in sortedKey:
#         sortedDict[w] = dictionary[w]

#     return sortedDict


# # print(valueDict(dictionary))
# sortedDict = valueDict(dictionary, True)
# print(sortedDict)





#5. Write a Python function to remove all the occurrences of a specified item from an array
# array = [1, 0, 3, 0, 2, 1, 3,]
# #number that will be removed
# val = 1

# def byeItem(array, removedVal):
   
#     #loop to remove all occurences, while true it will remove all 'removedVal'
#     try:
#         # Using while loop
#         while True:
#             array.remove(removedVal)

#         # Using for loop
#         # for element in array:
#         #     if(element == removedVal):
#         #         array.remove(element)
#     except ValueError:
#         #loop ends
#         pass
#     return (array)

# #prints new array without the number
# print(byeItem(array, val))


#6. Write a Python function to sum all the items in an array of numbers

# arr = [1, 2, 3, 4, 5, 6, 7]

# def sumArray(array):
#     s = 0

#     # for i in range(0, len(array)):
#     #     s = s + array[i]

#     # for element in array:
#     #     s = s + element

#     s = sum(array)

#     return(s)

# sum = sumArray(arr)
# print("Sum of all the elements of an array:" + str(sum))







#7. Write a Python function to sum all the items' value from a dictionary
# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}
# dict1 = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}
# def sumDict(dictionary):

   
#     values = dictionary.values()
#     print(values)
#     #returns value of dictionary
#     total = sum(values)
#     #adds to get the sum from all items
#     return(total)

# #prints the sum
# print(sumDict(dict1))





#8. Write a Python function to get the maximum and minimum value in a dictionary
# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}
# dict1 = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}
# def maxMinDict(dictionary):
   

#     # keyMax = max(dictionary.keys(), key=(lambda k: dictionary[k]))
#     # keyMin = min(dictionary.keys(), key=(lambda k: dictionary[k]))
#     # return (dict1[keyMax], dict1[keyMin])

#     keyMax = max(dictionary, key= dictionary.get)
#     keyMin = min(dictionary, key= dictionary.get)
#     return (dictionary[keyMax], dictionary[keyMin])

# result = maxMinDict(dict1)
# print("Max value:", result[0])
# print("Min value:", result[1])

#9. Write a Python function to merge 2 dictionaries
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}


# def mergeDict(dd1, dd2):

#     dd1 = {'a': 100, 'b': 200}
#     dd2 = {'x': 300, 'y': 200}

#     dd1.update(dd2)
#     return(dd1)

# print(mergeDict(d1, d2))

#10. Write a Python function to multiply all the items' value with 2 in a dictionary
# dictionary = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}
# d = {1: 40, 2: 20, 3: 30, 4: 10, 5: 60, 6: 50}
# def multiDict(diction):
#     # tot is how much it will be multiplied
#     tot=2
#     # diction.update((x , y*tot)for x, y in diction.items())

#     for key in diction:
#         # times all the items in the dictionary and prints it.
#         diction[key] = diction[key] * tot
#     return(diction)

    

# print(multiDict(d))