def alphacount(s):
    mydict={}
    for item in s:
        mydict.update({item:s.count(item)})
    return mydict
str = input("Enter a string : ")
print(alphacount(str))
