"""
name -> marks

"""

a = {
    "Neeraj": {
        "roll_num": 123,
        "gender": "Male",
        "math": 89,
        "chemistry": 90,
        "science": 88,
    },
    "Raj": {
        "roll_num": 123,
        "gender": "Male",
        "math": 89,
        "chemistry": 90,
        "science": 88,
    },
    "Naaj": {
        "roll_num": 123,
        "gender": "Male",
        "math": 89,
        "chemistry": 90,
        "science": 88,
    },
}

b = {
    "Neeraj": {
        "roll_num": 123,
        "gender": "Male",
        "marks": [89, 90, 87, 32, 58],
    },
    "Raj": {
        "roll_num": 123,
        "gender": "Male",
        "marks": [89, 90, 87, 32, 58],
    },
    "Naaj": {
        "roll_num": 123,
        "gender": "Male",
        "marks": [89, 90, 87, 32, 58],
    },
}

c = {
    "Neeraj": {
        "roll_num": 123,
        "gender": "Male",
        "marks": {"maths": 79, "science": 58, "hindi": 88},
    },
    "Raj": {
        "roll_num": 123,
        "gender": "Male",
        "marks": {"maths": 49, "science": 58, "hindi": 88},
    },
    "Naaj": {
        "roll_num": 123,
        "gender": "Male",
        "marks": {"maths": 19, "science": 58, "hindi": 88},
    },
}
# print(a["Neeraj"]["gender"])

for name, details in c.items():
    total = sum(details["marks"].values())
    print(f"{name} -> {total}")


