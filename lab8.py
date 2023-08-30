FileName = input("Please enter the ciphertext file name: ")

UserFile = open(FileName, "r")

CharCount = dict()

count = 0

countme = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for line in UserFile:
    line = line.upper()
    for char in line:
        if char in countme:
            if char in CharCount:
                CharCount[char] = CharCount[char] + 1
                count = count + 1
            else:
                CharCount[char] = 1
                count = count + 1

print("The character frequency findings are: ")
for C in CharCount:
    freq = CharCount[C] / count
    print(C + ": " + str(freq))


UserFile.close()
