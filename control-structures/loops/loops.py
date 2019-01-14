 # The BREAK STATEMENT - Used to immediately leave the body of its loopself.

for i in [12, 16, 17,24]:
    if i % 2 == 1:  # if the number is odd
        break  # immediately exit the loop
    print(i)
print("done")

# CONTINUE STATEMENT - causes the program to immediately skip the processing of the body of the loop  for the current iteration. But the loop still carries on running for its remaining iterations:

for i in [12, 16, 17,24]:
    if i % 2 == 1:  # if the number is odd
        continue  # Dont process it
    print(i)
print("done")

# Nested Loops for nested DATA

students = [("Beth",["BBIT", "IT"]),
            ("Cate",["BSCIT", "ECNM", "Music"]),
            ("Asha",["BCOM", "Acnts", "Dance", "Boxing"])]

# print all students with a count of their couses
for (name, subjects) in students:
    print(name, "takes", len(subjects), "courses")
