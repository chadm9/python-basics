import os

phonebook_data = {"Melissa": "404-235-5428", "Joe": "404-235-2125", "Mike": "770-134-2229", "Igor":"770-233-3461"}




def getInteger():
    try:
        input = int(raw_input("Enter your selection"))
        return input
    except:
        print "Invalid input.  Please provide an integer."
        return getInteger


def lookUp():
    input = raw_input("Enter a name to look up: ")
    if not phonebook_data.has_key(input):
        print "Name not in phonebook"
    else:
        print "Name: % \n Phone Number: %" % (input, phonebook_data[input])

def newEntery(phonebook_data):
    name = raw_input("Enter a name: ")
    number = raw_input("Enter a phone number: ")
    phonebook_data[name] = number
    return phonebook_data


def deleteEntry(phonebook_data):
    input = raw_input("Enter the name to delete: ")
    if not phonebook_data.has_key(input):
        print "Name not found in phonebook."

    else:
        del phonebook_data[input]

def listAll(phonebook_data):
    print phonebook_data


def quit():
    return exit()



while True:
    print '''Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Search for an entry
6. Quit'''
    selection  = getInteger()

    if selection == 1:
        lookUp()

    if selection == 2:
        newEntery(phonebook_data)

    if selection == 3:
        deleteEntry(phonebook_data)
        print phonebook_data

    if selection == 4:
        listAll(phonebook_data)




    if selection == 6:
        quit()



