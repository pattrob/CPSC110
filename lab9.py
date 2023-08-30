from random import seed, randint

def main():
    Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

    UserMessage = input("Please enter your message: ")

    EncryptorDecrypt = input("Please enter an E to encrypt or a D to decrypt: ")

    if EncryptorDecrypt == 'E':
        Encrypt = True
        print("The random key is: ")
        key = Make_Random_Key(len(UserMessage), Alpha)
        print(key)
        print("Make sure to copy the key down or you won't be able to decrypt.")
    elif EncryptorDecrypt == 'D':
        Encrypt = False
    else:
        print("Error, I didn't understand that input.")
        exit()


    if Encrypt == True:
        Ciphertext = ""
        i = 0
        while i < len(UserMessage):
            symbol = UserMessage[i]
            shift = Alpha.find(key[i])
            Pos = Alpha.find(symbol)
            NewPos = Pos + shift
            if NewPos >= len(Alpha):
                NewPos = NewPos - len(Alpha)
            Ciphertext = Ciphertext + Alpha[NewPos]
            i = i + 1

    else:
        key = input("Please enter the key: ")
        Plaintext = ""
        i = 0
        while i < len(UserMessage):
            symbol = UserMessage[i]
            Pos = Alpha.find(symbol)
            shift = Alpha.find(key[i])
            NewPos = Pos - shift
            if NewPos < 0:
                NewPos = NewPos + len(Alpha)
            Plaintext = Plaintext + Alpha[NewPos]
            i = i + 1



    if Encrypt == True:
        print("The ciphertext is: " + Ciphertext)
    else:
        print("The plaintext is: " + Plaintext)



def Make_Random_Key(Length_Key, Alpha):
    Key = ""
    alength = len(Alpha)
    i = 0
    while i< Length_Key:
        char = Alpha[randint(0,alength-1)]
        Key = Key + char
        i =i + 1
    return Key

if __name__ == '__main__':
    main()
            
        
            
