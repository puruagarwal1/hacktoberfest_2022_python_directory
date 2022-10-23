def fibonachi(x):
    n1, n2 = 0, 1
    count = 0
    print("Fibonacci sequence is:")
    while count < x:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
x = int(input("Enter n: "))
fibonachi(x)
