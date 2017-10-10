def apakahPrima(x) :	        
    prim = True	                
    if x >= 2 :	                
        for i in range(2, x):	
            if x % i == 0 :	
                prim = False	
    else :	                
        prim = False	        
    return prim	                

#>>> apakahPrima(100)
##False
##>>>

def cariFaktorPrima(n):
    ##n = 7824864274272489
    f, fs = 3, []
    while n % 2 == 0:
        fs.append(2)
        n /= 2
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += 2
    if n > 1: fs.append(n)
    return fs

##>>> cariFaktorPrima(7824864274272489)
##[3, 2608288091424163]
##>>>
