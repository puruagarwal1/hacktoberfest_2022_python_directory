x=input("Enter a number: ")
rev=x[::-1]
sum=0
for i in rev:
    sum+=int(i)
print(f"Reverse: {rev} and the sum: {sum}")