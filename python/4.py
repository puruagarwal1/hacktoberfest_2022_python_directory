cc = input("Enter your Credit Card Number: ")
l = len(cc);d4 = ""
for i in range(-4,0):
    d4 +=cc[i]
print("*"*(l-4)+d4)