Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'!?."

Ciphertext = input("Please enter a single line of encrypted ciphertext: ")

MyFile = open("lab6.txt", "w")

Currentkey = 0
while Currentkey < 66:
    Plaintext = ""
    for symbol in Ciphertext:
        if symbol in Alpha:
            pos = Alpha.find(symbol)
            Newpos = pos - Currentkey
            if Newpos < 0:
                Newpos = Newpos + len(Alpha)
            Plaintext = Plaintext + Alpha[Newpos]
        else:
            Plaintext = Plaintext + symbol

    MyFile.write(Plaintext)
    MyFile.write("\n")
    Currentkey = Currentkey + 1

MyFile.close()
