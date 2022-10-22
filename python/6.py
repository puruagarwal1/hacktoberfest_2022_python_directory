def doub(s1):
    s2=""
    for alphabet in s1:
        s2 = s2+alphabet+alphabet
    return s2
st = input('Enter String: ')
print(doub(st))