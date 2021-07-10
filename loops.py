
#1. Write a Python function to reverse the order of the items from an array
# array1 = [1, 2, 3, 4, 5, 6, 7]
# array1.reverse()
# print(array1)

#2. Write a Python function to sort an array by ascending or descending

# isAsc = input("ASC or DESC? ")
# array = [13, 24, 366, 1, 2,]
# def sortArray(_array, _isAsc):
    
#     if _isAsc.lower() == "asc":
#         # Ascending => asc
#         _array.sort()
#         return _array
#     else:
#         # Descending => desc
#         _array.sort(reverse= True)
#         return _array
        

# isAsc = "asc"
# print(sortArray(array, isAsc))
#3. Write a Python function to return the appearance of a specified element in an array
array3 = [3, 7, 2, 1, 8, 3, 9, 2, 1]
numberCount = int(input("Type number you want to count: "))
count = array3.count(numberCount)
# Ternary Operator
s = 's' if count > 1 else ''
print(f"This number appears {count} time{s}. And it is {count} time{s}")

# #5. Write a Python function to remove all the occurrences of a specified item from an array
# array4 = [2, 4, 7, 5, 8, 3, 2, 1, 2]
# numberRemove = int(input("Type number you want to remove: "))
# while array4.count(numberRemove) > 0:
#     array4.remove(numberRemove)
# print(array4)


# #6. Write a Python function to sum all the items in an array of numbers
# array5 = [2, 7, 5, 9, 3, 4, -18, -20, 2.5, 3.9]
# print(sum(array5))





