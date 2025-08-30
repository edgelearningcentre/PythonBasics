def total_marks(maths,science,english,hindi,history):
    total = maths+science+english+hindi+history
    print(total)


total_marks(89,74,84,11,23)  # named arguments
total_marks(english=100,history=88,science=11,maths=99,hindi=76)