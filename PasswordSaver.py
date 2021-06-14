import csv
import sys

#The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]


#The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

#The encryption key for the caesar cypher
encryptionKey=16

#Caesar Cypher Encryption
def passwordEncrypt (unencryptedMessage, key):

    #We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    #For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage

def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)



while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print(" 7. To delete a password")
    print("Please enter a number (1-7)")
    choice = input()

    if(choice == '1'): #Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'): #Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

#step 1 - loops through the list of passwords
        for i in range(len(passwords)):
#step 2 - checks if the name is found
            if passwordToLookup == passwords[i][0]:
#step 3 - prints out the passwords through encryption
                print(passwordEncrypt(passwords[i][1], -16))

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

#step 1 - encrypts the new password
        encryptedPassword = passwordEncrypt(unencryptedPassword, 16)
#step 2 - creates a list including the website name and encrypted password
        newPassword = [website, encryptedPassword]
#step 3 - adds the new password to the list
        passwords.append(newPassword)

    if(choice == '4'): #Save the passwords to a file
            savePasswordFile(passwords,passwordFileName)


    if(choice == '5'): #print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if(choice == '6'):  #quit our program
        sys.exit()

#delete a password
if (choice == '7'):

        print('Which website password do you wish to remove? ')
        for keyvalue in passwords:
            print(keyvalue[0])
        websiteChoice = input()
        passwordToRemove = [i for i in websiteChoice if i in passwords]

        for passwordToRemove in (passwords):
            passwords.remove(passwordToRemove)
        print('Your password for ' + str(websiteChoice) + ' has been successfully removed.')

print()
print()
