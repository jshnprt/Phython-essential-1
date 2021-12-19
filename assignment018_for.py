n=int(input("enter a number: "))
print("the divisor of the given number are:")
for i in range (1,n//2+1):
    if (n%i)==0:
        print(i,end=", ")
print(n)

    
