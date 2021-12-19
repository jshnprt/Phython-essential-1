even=-1
odd=0
n=1
while n!=0:
    n=int(input("enter the number: "))
    if n%2==0:
        even=even+1
    else:
        odd=odd+1
print("the count of even is: ",even)
print("the count of odd is: ",odd)
