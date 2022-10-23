x = int(input('Enter a number: '))
print("\n1st Pattern\n")
for i in range(x+1):
    print("*"*i)
print("\n2nd Pattern\n")
for i in reversed(range(x+1)):
    print("*"*i)
print("\n3rd Pattern\n")
for i in range(x+1):
    for j in range(i):
       print(f"{j+1}",end="") 
    print("")
print("\n4th Pattern\n")
for i in reversed(range(x+1)):
    for j in range(i):
       print(f"{j+1}",end="") 
    print("")
print("\n5th Pattern\n")
for i in range(x+1):
    for j in range(i):
       print(f"{j+1}",end="") 
    print("")
print("\n6th Pattern\n")
for i in range(x+1):
    print(f"{i}"*i)
print("\n7th Pattern\n")
for i in reversed(range(x+1)):
    print(f"{x+1-i}"*i)
print("\n8th Pattern\n")
a=1
b=x
for i in range(x+1):
    if(a>x):
        print(" "*(i),end="")
        print("*"*b)
        b-=2
    else:    
        print(" "*(x-i),end="")
        print("*"*a)
        a+=2
    
    
    