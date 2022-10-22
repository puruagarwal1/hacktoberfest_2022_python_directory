def todict(s):
    f=0;mydict={};set1= set(s)
    for item in s:
        mydict.update({item:s.count(item)})
    return mydict
st = 'google.com'
print((todict(st)))