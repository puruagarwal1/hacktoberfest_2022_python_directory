def alphacount(str):
    mydict={}
    for item in str:
        mydict.update({item:str.count(item)})
    return mydict
str = input("Enter a string : ")
print(alphacount(str))
