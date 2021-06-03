#Caesar Cypher Encryption

#Get the message to encrypt from the user
print('Enter your message:')
unencryptedMessage = input()

#Get the encryption key from the user.  Note the error handling to make sure we have a number from 1-26
key=0
while (key < 1 or key > 26):
    print('Enter the key number (1-26)')
    key = int(input())

print('The key is ' + str(key))

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

print("Your encrypted message is:")
print(encryptedMessage)
