# Write a Python program to count the number 4 in a given list.

n = int(input("Please enter the length of the list: "))

print("Please enter the list numbers: ")
lst = [int(input()) for _ in range(n)] 

print(f"The number of occurrences of 4 is: {lst.count(4)}")