# Python uses the flow control statements
# if statement
Number = int(input(" Enter a Number: ")) # int command convert the input number into integer
                                         # input command is used to enter a number value from the user end.
if Number < 0:
    print('Number is Negative')
elif Number == 0:                       # elif is a short form of else if command
    print('Sorry Number is Zero')       # elif is a nesting of if and else statement
elif Number > 0:
    print('Number is Positive')
else: 
    print('Its enough')

#-----------------------------------------------------------------------------------------------
# for statement
"""
The for statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always iterating over an arithmetic progression (A.P.) or giving the user the ability to 
define both the iteration step and halting condition.
For statment iterates over the items of any sequence.
"""
Cricket_Accesories = ['Bats', 'Balls', 'Pitch','Gloves']
for items in Cricket_Accesories:
    print(items,len(items))


# creata a sample collection
userdata = {'Bats':'active','Balls':'inactive','Gloves':'active'}

# strategy : iterate over a copy 
for user , status in userdata.copy().items():
    if status == 'inactive':
        del userdata[user]

# strategy : create a new collection
active_users = {}
for user, status in userdata.items():
    if status == 'active':
        active_users[user] = status
        print(active_users)
