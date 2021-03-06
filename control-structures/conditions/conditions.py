# While - repeats a body of code as long as condition is true

counter = 1
while counter <= 5:
    print("Hello, World")
    counter = counter + 1

# if BOOLEAN EXPRESSION:
#     STATEMENTS
food = "chapati"
if food == "chapati":
    print("My favourite!")

# if-else STATEMENT

food = "chips"
if food == "chapati":
    print("My favourite!")
else:
    print("I want chapo!")

# The For loop STATEMENT (Each item in turn is re-assigned to the loop variable and the body is executed)
# # general format =
#                     for LOOP_VARIABLE in SEQUENCE:
#                         STATEMENTS

for friend in ['Nama', 'Cate', 'Sue']:
    invitation = "Hi" + friend + ". Please come to my party on Sat!"
    print(invitation)

# BOOLEAN  DATA OBJECTS
print(5 == 10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))

# feature that allows you control the flow of your program based on the value of a variable or an expression.
# The Pythonic way to implement switch statement is to use dictionary mappings.

def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
     }
    print(switcher.get(argument, "Invalid month"))


switch_demo(6)
