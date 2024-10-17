#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.
favorite_foods = ["Pizza", "Pasta", "Sushi", "Burgers", "Ice Cream"]

favorite_foods.extend(["Tacos", "Fried Chicken"])

favorite_foods.remove("Burgers")
print("Updated list of favorite foods:", favorite_foods)




#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

numbers = [2, 5, 8, 10, 3, 6]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Reversed list:", numbers[::-1])

sum_of_numbers = sum(numbers)
print("Sum of all elements:", sum_of_numbers)
