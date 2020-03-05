p=float(input("Enter the principal :"));
rate=float(input("Enter the rate :"));
time=int(input("Enter the time :"));
n=int(input("Enter the compounding period :"));
amount=p*(1+rate/(100*n))**(n*time);
interest=amount-p;
print("The required interest is :","%.2f"%interest);
print("The required amount is :","%.2f"%amount);
