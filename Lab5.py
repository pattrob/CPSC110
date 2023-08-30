Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."



UserMessage = input("Please enter a message: ")

EncryptOrDecrypt = input("Please enter a D to decrypt or an E to encrypt: ")


if EncryptOrDecrypt == "E":
    Encrypt = True
elif EncryptOrDecrypt == "D":
    Encrypt = False
else:
    print("Error, I didn't understand that input.")
    exit()


key = int(input("Please enter an interger for the key: "))

if Encrypt == True: 
    Ciphertext = ""

    
    for symbol in UserMessage:
        if symbol in Alpha:
            pos = Alpha.find(symbol)
            NewPos = pos + key
            if NewPos >= len(Alpha):
                NewPos = NewPos - len(Alpha)
            Ciphertext = Ciphertext + Alpha[NewPos]
        else:
            Ciphertext = Ciphertext + symbol

else:
    Plaintext = ""
    for symbol in UserMessage:
        if symbol in Alpha:
            pos = Alpha.find(symbol)
            NewPos = pos - key
            if NewPos < 0:
                NewPos = NewPos + len(Alpha)
            Plaintext = Plaintext + Alpha[NewPos]
        else:
            Plaintext = Plaintext + symbol



if Encrypt == True:
    print(Ciphertext)
else:
    print(Plaintext)
                    
            
            
                
        
        
          
