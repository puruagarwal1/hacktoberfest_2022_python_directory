from audioop import reverse


def fun(choice,list1):
    if choice == 'asc':
        list1.sort()
        return(list1)
    elif choice == 'desc':
        list1.sort()
        list1.reverse()
        return(list1)
    else:
        return(list1)

l=[10,56,20,5,4,70,100,30,34,27,7]
f=['asc','desc','none']
ch = input(f'Enter Choice from{f} :  ')
l2 = fun(ch,l)
print(l2)
