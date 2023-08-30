def main():
    PlaintextAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
    CipherAlpha = "KLM789AghijklmBIXYZabcdefno0 !?pCDEFGHqrstuvwxJNOPQRSTUVWyz123456."
    X = Find_Cipher_Char(PlaintextAlpha, CipherAlpha, 'A')
    print(X)
    X = Find_Cipher_Char(PlaintextAlpha, CipherAlpha, 'a')
    print(X)
    X = Find_Cipher_Char(PlaintextAlpha, CipherAlpha, '0')
    print(X)
    X = Find_Cipher_Char(PlaintextAlpha, CipherAlpha, '#')
    print(X)
    Y = input("Please enter a single character: ")
    print(Find_Cipher_Char(PlaintextAlpha, CipherAlpha, Y))

    



def Find_Cipher_Char(List1, List2, C):
    if len(List1) != len(List2):
        return -1
    else:
        i = 0
        Found = False
        Cpos = -1
        Cpos2 = -1
        while i < len(List1):
            Cpos = List1.find(C)
            break

            i = i + 1

        while i < len(List2):
            Cpos2 = List2.find(C)
            if Cpos2 == -1:
                 print("The encrypted character is not found: ")
                 return Cpos2
            print("The encrypted character is: ")
            return List2[Cpos]
            break

            i = i + 1
    
        

        
if __name__ == '__main__':
    main()


              
            
        

