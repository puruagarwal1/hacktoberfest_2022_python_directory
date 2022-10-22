def fun(l2):
    
    for item in l2:
        if type(item) is str:
            l2.remove(item)         
    return l2


l1=[-5,"lakhu","asg","Bhaiya",'arit',-79,"arpit",-78,-100,"Error"]
print(fun(l1))