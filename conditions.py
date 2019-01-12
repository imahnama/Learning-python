# While - repeats a body of code as long as condition is true

counter = 1
while counter <= 5:
    print("Hello, World")
    counter = counter + 1

# if BOOLEAN EXPRESSION:
#     STATEMENTS
food ='chapati'
if food == 'chapati':
    print('My favourite!')

# if-else STATEMENT

food ='chips'
if food == 'chapati':
    print('My favourite!')
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
print(5==10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))

# Switch STATEMENT - is a multiway branch statement that compares the value of a variable to values specified in case statements
# Py dsnt have switch statement it uses dictionary mapping to implement switch statement

var = input("enter a number between 1 and 5")
def switch_demo(var):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "June",
        5: "July"
     }
     print switcher.get(var, "Invalid month")
