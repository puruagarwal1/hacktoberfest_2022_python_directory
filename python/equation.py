def delta(a,b,c):
    delta = (b**2) - (4*a*c)
    return {"delta":delta}

def raizes(a,b,c,delta):
    x1 = (-b+ delta**(1.0/2.0)) / (2.0*a)
    x2 = (-b- delta**(1.0/2.0)) / (2.0*a)
    return {"x1":x1,"x2":x2}
