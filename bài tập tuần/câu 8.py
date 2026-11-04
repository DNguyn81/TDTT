a=input("Ten chu ho:")
b=int(input("Chi so thang truoc:"))
c=int(input("Chi so thang nay:"))
d=c-b
if 0<=d<=50:
    d=1.08*(1984*d)
elif 51<=d<=100:
    d=1.08*(2050*d)
elif 101<=d<=200:
    d=1.08(2380*d)
elif 201<=d<=300:
    d=1.08(2998*d)
elif 301<=d<=400:
    d=1.08(3350*d)
elif d>=401:
    d=1.08(3460*d)
print("Ten chu ho:", a)
print("Tien phai tra:", int(d))
