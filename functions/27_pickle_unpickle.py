import pickle

class Student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age


s= Student("Neeraj",40)
# f = open("name.txt","wb")
# pickle.dump(s,f)
# f.close()

# for loading
f = open("name.txt","rb")
st = pickle.load(f)
print(st.name)
print(st.age) 



# write 
# x = " Code and Debug"

# with open('name.txt','w') as f :
#     f.write(str(s))


# read
# with open('name.txt', 'r') as f:
#     print(f.read())