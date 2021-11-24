print("a*x+b=0 formában levő első fokú egyenletet fogok most megoldani")
a=float(input("Kérem az x együtthatóját="))
b=float(input("Kérem a konstans tagot="))
if a==0 :
    if b==0 :
        print("Minden valós szám megoldás")
    else:
        print("Nincs megoldás")
else:
    x=-b/a
    print("A megoldás:",x)
    
    
