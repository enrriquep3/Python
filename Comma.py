listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)
for item in listToPrint[:-1]:
    print(item, end=', ')
print('and', listToPrint[-1])
