def cal(x,a,b):
    if x == '+' :
        return a+b
    elif x == '-' :
        return a-b
    elif x == '*' :
        return a*b
    elif x == '/' :
        return a/b
    elif x == '%' :
        return a%b
a,b=list(map(int, input("Enter 2 variables: ").split()))
x = input("Enter you choice (+,-,*,/,%): ")
result=cal(x,a,b)
print(result)