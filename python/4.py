cci = input("Enter your Credit Card Number : ") 
l = len(cci)
d4=""
cc = ""
if l>16:
    for j in range(0,l):
        if cci[j]!=" ":
            cc +=cci[j]
else :
    cc=cci

len=len(cc)
if len==16:
    for i in range(-4,0):
        d4 +=cc[i]
    print("Your CC is "+ "**** "*3+d4)
else:
    print("Enter Valid CC number")