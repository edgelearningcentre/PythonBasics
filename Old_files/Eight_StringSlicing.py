# Slicing allows us to obtain substring from the main string

word = "Python Basics"
substring = word[0:6]       # characters from position 0 included and 6 is excluded
print(substring)            # output is Python

substring2 = word[7:]       # characters from position 7 included and end is excluded
print(substring2)           # output is Basics

# try it yourself and just uncomment the lines 12 to 19
# if you are using Visual Studio Code. Just select these lines and press ctrl + / to uncomment


# substring3 = word [:2]
# print(substring3)

# substring4 = word [4:]
# print(substring4)

# substring5 = word [-2:]
# print(substring5)

# Note Start is always included and end alwayss excluded.

substring6 = word[:2] + word[2:]
print(substring6)

substring7 = word[:4] + word[4:]
print(substring7)

'''
One way to remember how slices work is to think of the indices as pointing between characters
'''
