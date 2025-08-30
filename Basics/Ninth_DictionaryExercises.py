


# Exercise 1 : Convert two lists into dictionary

keys = ['Ten','Twenty','Thirty']

values = [11,21,31]

# print("lists are :")
# print(keys)
# print(values)


# Zip function 

result_dict = dict(zip(keys,values))
# print("resultant dictionary")
# print(result_dict)


# Exercise 2 : Merge two python dictionaries into one

# Method1
dict1 = {'Ten': 11, 'Twenty': 21, 'Thirty': 31}

dict2 = {'Fourty': 41, 'Fifty': 51, 'Sixty': 61}

dict3 = {**dict1,**dict2}     # asterik function for merging the dictionaries
# print(dict3)

#-----------------------------
# Method 2
dict4 ={}
dict4 = dict1.copy()
dict4.update(dict2)
# print(dict4)


# Exercise 3 : Print the value 80  of key 'history' from the below
# Nested dictionary

Sample_Dict = {
    "Class":{
        'student':{
            "name":"John",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}

# print(Sample_Dict)
# print(Sample_Dict['Class'])
# print(Sample_Dict['Class']['student'])
# print((Sample_Dict['Class']['student']['marks']))
# print((Sample_Dict['Class']['student']['marks']['history']))



# Exercise 4 : Intialize dictionary with default values

employees = ['John','Darick']
defaults = {"designation":'Developer','Salary':80000}

# fromkeys()

resultant_dict = dict.fromkeys(employees,defaults)

# print(resultant_dict)

# expectation : {'John':{"designation":'Developer','Salary':80000},'Darick':{"designation":'Developer','Salary':80000}}


# Exercise 5 : Rename key of a dictionary   rename  'adnbd' to 'location'
demographic_data = {
    "Name":'John',
    "Age":25,
    "Salary":7000,
    "adnbd": "New York"
}

print(demographic_data)
# del demographic_data['New York'][0]
# demographic_data['location'] = del demographic_data['adnbd']  # we can't use replace and remove for dict keys 

demographic_data['location'] = demographic_data.pop('adnbd')  # we can't use  commands 'replace' and 'remove' for dict keys 
print(demographic_data)

