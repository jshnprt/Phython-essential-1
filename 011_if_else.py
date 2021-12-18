a=float(input("Enter your income: "))
if a<85528:
    b=(0.18*a)-556.02
    if b<=0:
        print("There is no money return")
    else:
        print("The tax is: ",b)
else:
    print("The tax is: ",14839.02+((a-85525)*0.32))
