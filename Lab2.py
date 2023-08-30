def TempConvert():
    Ctemp=(Ftemp-32)*(5/9)
    return Ctemp





Ftemp = int(input("Please enter a temperature in degrees Farenheit: "))

Ctemp = TempConvert()


print(Ctemp)
