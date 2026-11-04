c = input("Nhập vào một kí tự in hoa:")
if c == 'A':
    print(c)
elif 'B' <= c <= 'Z':
    c=chr(ord(c)+31)
    print(c)
    
