file_name = input("Enter file name = ")

file_name = file_name + ".txt"

with open(file_name,"w") as f:
    while True:
        sentence = input("Enter  a sentence = ")
        if sentence == "q" or sentence =="Q":
            break
        f.write(sentence)
        f.write("\n")
