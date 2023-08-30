print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

Tcount1 = name1_lower.count("t")
Tcount2 = name2_lower.count("t")
Ttotal = Tcount1 + Tcount2

Rcount1 = name1_lower.count("r")
Rcount2 = name2_lower.count("r")
Rtotal = Rcount1 + Rcount2

Ucount1 = name1_lower.count("u")
Ucount2 = name2_lower.count("u")
Utotal = Ucount1 + Ucount2

Ecount1 = name1_lower.count("e")
Ecount2 = name2_lower.count("e")
Etotal = Ecount1 + Ecount2

truecount = Ttotal + Rtotal + Utotal + Etotal


Lcount1 = name1_lower.count("l")
Lcount2 = name2_lower.count("l")
Ltotal = Lcount1 + Lcount2

Ocount1 = name1_lower.count("o")
Ocount2 = name2_lower.count("o")
Ototal = Ocount1 + Ocount2

Vcount1 = name1_lower.count("v")
Vcount2 = name2_lower.count("v")
Vtotal = Vcount1 + Vcount2

Eecount1 = name1_lower.count("e")
Eecount2 = name2_lower.count("e")
Eetotal = Eecount1 + Eecount2

lovecount = Ltotal + Ototal + Vtotal + Eetotal

totalcount = str(truecount) + str(lovecount)

intcount = int(totalcount)


if intcount <= 10 or intcount >= 90:
  print(f"Your score is {totalcount}, you go together like coke and mentos.")
elif intcount >= 40 and intcount <= 50:
  print(f"Your score is {totalcount}, you go alright toghether.")
else:
  print(f"Your score is {totalcount}.")


