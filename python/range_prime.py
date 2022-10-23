        
x,y = input("Enter the Range: ").split()
print("Prime Numbers in the Range are: ")
for i in range(int(x),int(y)+1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i)
