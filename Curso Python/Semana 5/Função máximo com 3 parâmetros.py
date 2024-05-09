def maximo(x,y,z):    
    if y < x > z:
        return x
    elif x < y > z:
        return y
    elif y < z > x:
        return z
    elif x == z == y:
        return x
    elif y == x > z:
        return x
    elif y == z > x:
        return z
    elif x == z > y:
        return z