s=#enter string
k=#amount to shift by
new=''
for i in s:
    if ord(i) in range(97,123):
        y=ord(i)+k
        if (y>122):
            while (y>122):
                y=y-26
            x=chr(y)
        else:
            x=chr(ord(i)+k)
        new=new+x
    elif ord(i) in range(65,91):
        z=ord(i)+k
        if z>90:
            while(z>90):
                z=z-26
            x=chr(z)
        else:
            x=chr(ord(i)+k)
        new=new+x
    else:
        new=new+i
print(new)
