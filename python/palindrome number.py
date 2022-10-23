s=int(input("Enter a number: "))
num=s
while s!=0:
    rem=s%10
    rev=int(rev*10+rem)
    s=int(s/10)
if num==rev :
    print("Palindrome")
else:
    print("Not Palindrome")