
""" Python can manipulate strings, which can be expressed in three ways
enclosed in single quotes '....'
enlcosed in double quotes "...."
.\ can be used to escape quotes
"""

Date = '10-Feb-2022'        # Single Quotes
print(Date)

word = 'doesn\'t'            # use \' to escape to single quote
print(word)

word1 = "doesn't"           # use double quotes 
print(word1)

word2 = 'First Line.\n Second Line.'   # \n means newLine
print(word2)

# Raw Strings 

print('C:\some\name')      # here \n means new line

print(r'C:\some\name')     # note the r before the quote
