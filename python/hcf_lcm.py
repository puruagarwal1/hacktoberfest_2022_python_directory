def hcf(x, y):
    smaller = min(x,y)
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
def lcm(x,y):
    maxno = max(x,y)

    while(True):
        if((maxno % x == 0) and (maxno % y == 0)):
            lcm = maxno
            break
        maxno += 1

    return lcm
x,y = input('Enter 2 Numbers: ').split()

print("The H.C.F. is ", hcf(int(x),int(y)))
print(" The L.C.M is ", lcm(int(x),int(y)) )
