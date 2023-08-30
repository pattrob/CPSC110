InputString = input("Please enter a string: ")

Length = len(InputString)

i = Length - 1

OutPutString = ""


while i >= 0:
    OutPutString = OutPutString + InputString[i]
    i = i-1

print(OutPutString)
    



