Input_String = input("Please enter a string: ")

ch_string = []

ch_count = 0

for character in Input_String:
    if character not in ch_string:
        ch_count = ch_count + 1
        ch_string.append(character)


print("The number of distinct characters is: " + str(ch_count))

    
