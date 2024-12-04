# 1. Write a Python program to find the sum of all elements in a list.


numbers = [1, 2, 3, 4, 5]

total_sum = sum(numbers)

print("Sum of all elements:", total_sum)


# 2. Write a Python program to remove duplicates from a list.


arr = [1, 2, 1, 2, 3, 4, 3]

unique_elements = list(set(arr))

print("List with duplicates removed:", unique_elements)



# 3. Write a Python program to find the second largest element in a list.


arr = [10, 20, 4, 45, 99]

arr.sort()

second_largest = arr[-2]

print("Second largest element:", second_largest)


# 4. Write a Python program to count the occurrences of each element in a list.


arr = [1, 2, 2, 3, 3, 3, 4]

occurrences = {i: arr.count(i) for i in arr}

print("Occurrences of each element:", occurrences)

# 5. Write a Python program to reverse a list.


arr = [1, 2, 3, 4, 5]

arr.reverse()

print("Reversed list:", arr)

# 6. Write a Python program to find the maximum and minimum elements in a list.

arr = [10, 20, 4, 45, 99]

maximum = max(arr)

minimum = min(arr)

print("Maximum element:", maximum)

print("Minimum element:", minimum)

# 7. Write a Python program to merge two lists and sort the resulting list.

arr1 = [1, 4, 6]

arr2 = [2, 5, 3]

merged_list = sorted(arr1 + arr2)

print("Merged and sorted list:", merged_list)


# 8. Write a Python program to find common elements in two lists.

arr1 = [1, 2, 3, 4]

arr2 = [3, 4, 5, 6]

common_elements = list(set(arr1) and set(arr2))

print("Common elements:", common_elements)

# 9. Write a Python program to check if a list is empty.

arr = []

if not arr:

    print("The list is empty")

else:

    print("The list is not empty")


# 10. Write a Python program to remove an element from a list by index.

arr = [10, 20, 30, 40, 50]

index = 2  # Remove element at index 2 (30)

arr.pop(index)

print("List after removing element:", arr)


# 11. Write a Python program to find the length of a list without using the len() function.

arr = [1, 2, 3, 4, 5]

length = 0

for _ in arr:

    length += 1

print("Length of the list:", length)


# 12. Write a Python program to multiply all elements in a list.

arr = [1, 2, 3, 4]

result = 1

for num in arr:

    result *= num

print("Product of all elements:", result)


# 13. Write a Python program to find all the even numbers in a list.

arr = [1, 2, 3, 4, 5, 6]

even_numbers = [num for num in arr if num % 2 == 0]

print("Even numbers:", even_numbers)


# 14. Write a Python program to replace an element in a list with another element.

arr = [1, 2, 3, 4, 5]

index = 2  # Replace element at index 2

arr[index] = 10  # Replace 3 with 10

print("List after replacement:", arr)


# 15. Write a Python program to split a list into two halves.

arr = [1, 2, 3, 4, 5, 6]

mid = len(arr) // 2

first_half = arr[:mid]

second_half = arr[mid:]

print("First half:", first_half)

print("Second half:", second_half)


