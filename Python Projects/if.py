print("welcome to weight calculator")
weight=float(input("enter your weight" ))
unit=input("in LBS OR KG")
if unit.upper=="KG":
    convert=weight*2.205
    print("your weigt in kg is:",convert)
else:
    convert=weight/2.205
print("your weight :",convert)



