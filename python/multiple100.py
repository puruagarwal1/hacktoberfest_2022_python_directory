s=int(input("Enter a Number: "))
for i in range(1,21):
    if s*i > 100:
        break
    print(s*i)
