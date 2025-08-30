## Ask Subject name and marks from the user and keep adding it to dictionary


# num_subjects = int(input("Enter the number of subjects = "))
# marks = {}
# for _ in range(0,num_subjects):
#     sub_name = input("Enter name of the Subject = ")
#     sub_marks = int(input(f"Enter marks for {sub_name} = "))
#     marks[sub_name] = sub_marks
#     # marks.update({sub_name:sub_marks})

# print(marks)


## Convert two lists into a dictionary

# lst1 = ["Ten", "Twenty", "Thirty"]
# lst2 = [10, 20, 30]

# output= {}

# for i in range(0,len(lst1)):
#     for j in range(0,len(lst2)):
#         output[lst1[i]] =  lst2[j]

# print(output)

## Write a python program to sum all items in a dictionary

# marks = {
#     "physics": 78,
#     "english": 91,
#     "computer": 43,
#     "history": 19,
#     "chemistry": 73,
# }

# total = 1

# for v in marks.values():
#     total = total * v

# print(total)
# print(sum(list(marks.values())))

## Display the dictionary where each key is a character
#  and value is the frequency of that character that comes
#  in that string

# frequency = {}
# user_string = input("Enter string by the user = ")

# for ch in user_string:
#     if ch in frequency:
#         frequency[ch]+=1
#     else:
#         frequency[ch]=1

# print(frequency)


## Ques
"""
# Store "name" of the student as Key.
# "List of 5 marks" of that student as a value.
# Store atleast 5 student names.
# Print the sum and percentage of all the students
#"""


# students_data ={
#     "student1":[85,52,84,65,47],
#     "student2":[85,52,84,65,46],
#     "student3":[85,52,84,65,45],
#     "student4":[85,52,84,65,47],
#     "student5":[85,52,84,65,44],
# }

# for name,marks in students_data.items():
#     total =sum(marks)
#     percentage = total/500 * 100
#     print(f"{name} has scored total {total} marks and  percentage is {percentage:2f}")


"""
Store marks of 5 different subject in a dict. 
Ask subject name as input from the user.
Print the marks of that subject entered by user
if subject doesnot exist, print invalid

"""

subject_marks = {
    "Math": 90,
    "English": 85,
    "Science": 70,
    "History": 65,
    "Computer": 88,
}

subject_name = input("Enter subject name = ")

if subject_name in subject_marks:
    print(subject_marks[subject_name])

else:
    print("invalid")