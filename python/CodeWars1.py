# def to_camel_case(s):
#     s+="-"
#     l=[];a=0;b=0;st=""
#     for i in s:
#         if i == '-' or i == '_':
#             l.append(s[b:a])
#             b=a+1
#         a+=1
#     for item in l:
#         if item == l[0]:
#              st+=item
#              continue
#         st+=item.capitalize()
#     return st

def to_camel_case(s):
    return s[0] + s.title().translate(s.maketrans("", "", "-_"))[1:] if s else s
        

s= 'To_camel_case'
print(to_camel_case(s))