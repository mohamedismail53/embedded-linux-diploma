# Write a Python program to test whether a passed letter is a vowel or not.

vowels = ['a', 'e', 'i', 'o', 'u']

usrInput = input('Please enter a character:').strip()[0]
print(f'Your single character input was: {usrInput.lower() in vowels}')