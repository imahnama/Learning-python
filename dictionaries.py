#A set of Key: value pairs with unique keys.
#its a built-in data type in python
#They are indexed by keys, which can be any immutable type.

contacts = dict() #create empty dictionary contacts

contacts['Nama'] = '1234'
contacts['Ima'] = '2345'
contacts['Cate'] = '6799'
contacts['Mercy'] = '1289'

names = ['Nama', 'Ima', 'Cate', 'Mercy']

for name in names:
    if name in contacts:  #Check to see if each name from the list is in the dict
        print('My name is ' + name + ' and my number is ' + contacts[name])
    else:
        print('The number of ' + name + 'is unknown')


# Applying dictionary
#Dictionary Can be used to count no of onjects
# - Storage of any data associated with the object

#These two methods can be used to create small dict by listing all their elements
contacts = {'Nama': '1234', 'Ima': '2345'}
print(contacts)
contacts = dict(Nama = '1234', Ima = '2345')
print(contacts)

#Method to create large dict
contacts = dict(zip(["Nama", "Ima"], ["1234", "2345"]))
print(contacts)
contacts = dict([("Nama", "1234"), ("Ima","2345")])
print(contacts)

#Working with dictionary items

alphabets_position = {'a' : '1', 'b' : '2', 'c' : '3'}
exact_postion = alphabets_position['a'] #accessing using key
print(exact_postion)

#Adding a new value to a dictionary
alphabets_position['2'] = '10'
print(alphabets_position)

#removing an item from dictionary
winners = {'Nama' : '1', 'Ima' : '2', 'Cate' : '3'}
key = 'Sue'
if key in winners:
    del winners['Sue']

try:
    del winners['Sue']
except KeyError as position:
    print('Winner does not exist "' + key + '" in dict')
print(winners)
