
def main():
    TheList = ["Ancient Mariner", "Barracuda", "Blow My Skull Off", "Blue Hawaiian", "Cobra's Fang", "Fog Cutter", "Jungle Bird", "Mai Tai",
           "Mary Pickford", "Navy Grog", "Painkiller", "Planter's punch", "Scorpion bowl", "Suffering Bastard", "TestPilot" , "Zombie"]

    UserInput = input("Please Enter a string: ")


    Result = substring(TheList, UserInput)

    if Result[0]:
        print("Found at position " + str(Result[1]) + " of " + TheList[Result[2]])

    else:
        print("Not found")  




def substring(TheList, teststring):
    i = 0
    Found = False
    TempFindTest = -1
    while i < len(TheList):
        TempFindTest = TheList[i].find(teststring)
        if TempFindTest != -1:
            Found = True
            break
        
        i = i + 1
    return [Found, TempFindTest, i]



if __name__ == '__main__':
    main()


   



