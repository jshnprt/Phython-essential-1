hh1=int(input("Give me the start time hour:"))
mm1=int(input("Give me the start time minute:"))
d=int(input("Give me the duration in minutes:"))
f=hh1*60+mm1+d
hh2=f//60
mm2=f-hh2*60
print("The finish time is=",hh2,":",mm2)
