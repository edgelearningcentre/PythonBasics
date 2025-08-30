# my_dict = {
#     "name": "neeraj",
#     "age": 40,
#     "gender": "male",
#     "marks": 66.5,
# }

# print(my_dict)

# ## get a value
# print(my_dict["name"])
# print(my_dict.get("name"))


# k = input("Enter a key = ")

# result = my_dict.get(k)

# if result is not None:
#     print(result)
# else:
#     print("Key does not exist")

# print(my_dic

# my_dict = {
#     "history": 67,
#     "computer": 99,
#     "science": 78,
#     "maths": 11,
# }


# total = 0
# print(my_dict.keys())
# for v in my_dict.values():
#     total = total + v

# print(total)


"""
output should be like this 
name -> neeraj
age -> 40
"""

my_dict = {
    "name": "neeraj",
    "age": 40,
    "gender": "male",
    "marks": 66.5,
}

for k,v in my_dict.items():
    print(f"{k} -> {v}")

