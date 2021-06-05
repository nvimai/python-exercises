#1. Write a Python function to reverse the order of the items from an array
array1 = [1, 2, 3, 4, 5, 6, 7]
array1.reverse()
print(array1)

#2. Write a Python function to sort an array by ascending or descending
array = [13, 24, 366, 1, 2,]
array.sort()
print(array)

#3. Write a Python function to return the appearance of a specified element in an array
array3 = [3, 7, 2, 1, 8, 3, 9, 2, 1]
count = array3.count(2)
print(count)

#5. Write a Python function to remove all the occurrences of a specified item from an array
array4 = [2, 4, 7, 5, 8, 3, 2, 1, 2]
while array4.count(2) > 0:
    array4.remove(2)
print(array4)


#6. Write a Python function to sum all the items in an array of numbers
array5 = [2, 7, 5, 9, 3, 4, -18, -20, 2.5, 3.9]
print(sum(array5))



