a=float(input("Nhập số đo cạnh AB:"))
b=float(input("Nhập số đo cạnh BC:"))
c=float(input("Nhập số đo cạnh AC:"))
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))**(1/2)
if a<b+c and b<a+c and c<b+a:
    print("Diện tích tam giác:", S)
else: 
    print("Không phải 3 cạnh của tam giác")