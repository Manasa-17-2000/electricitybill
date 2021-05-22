#program to calculate eb bill
unit = unit = int(input("enter the unit : "))

if unit >= 0 and unit <= 30:
    charge = unit*3.75+(5/100)
    fixedcharge = 60
    final = charge + fixedcharge
    print("eletricity bill =" % final)

elif unit >= 30 and unit <= 100:
    charge = 5.2*unit+(5/100)
    fixedcharge = 60
    final = charge + fixedcharge
    print("eletricity bill =" % final)

elif unit >= 101 and unit <= 200:
    charge = 6.75*unit+(5/100)
    fixedcharge = 60
    final = charge + fixedcharge
    print("eletricity bill =" % final)

elif unit >201:
    charge = 7.8*unit+(5/100)
    fixedcharge = 60
    final = charge + fixedcharge
    print("eletricity bill =f"%final)
