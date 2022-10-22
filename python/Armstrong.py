x = (input("Enter the number: "))
temp = x
l = len(x)
arm =0
for i in x[:]:
    arm += int(pow(int(i),l))
if int(x) == arm:
    print("Armstrong Number")
else:
    print("Not Armstrong")

