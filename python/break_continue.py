def table(n):
    for i in range(15):
        if i == 0:
            continue
        elif i > 10:
            break
        print(f"{x} x {i} = {x*i}")

x = int(input("Enter a no.: "))
table(x)