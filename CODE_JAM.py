#=============================================
#A2

#cara 1
def permutasi(StringPertama, StringKedua):
   if (len(StringPertama) != len(StringKedua)):
      return False

   StringPertamaCount = 0
   StringKeduaCount = 0

   for char in StringPertama:
      StringPertamaCount += ord(char)

   for char in StringKedua:
      StringKeduaCount += ord(char)

   if StringPertamaCount == StringKeduaCount:
      return True

   return False

##>>> 
##>>> permutasi('abc','bcs')
##False
##>>> permutasi('abc','bca')
##True
##>>>

#cara 2
from collections import Counter
def permutasi2(a,b):
    if len(a) != len(b):
         return False
    return  Counter(a) == Counter(b)

##>>> 
##>>> permutasi2('abc','bca')
##True
##>>> permutasi('abc','bcs')
##False
##>>> 

#=============================================
#A3

##class fungsi ():
##    def __init__ (self):
##        self.bilangan = list ()
##
##    def get_amount(self , n ,p , q):
##        for i in range(1, n):
##            if (i % p == 0) or (i % q == 0):
##                self.bilangan.append(i)
##            else:
##                continue
##        return sum(self.bilangan)
##if __name__ == "__main__":
##    fg = fungsi()
##    print fg.get_amount(10,3,5)

#============================================
#A4

class bilangan():
    def __init__(self):
        self.nilai_kali = 1
        self.bilangan_terkecil = 0
        self.status = list()
        
    def dapatkan_bilangan(self, number):
        for num in range(1, number + 1):
            self.nilai_kali *= num

        for i in range (1, self.nilai_kali + 1):
            for j in range(1, number + 1):
                if i % j == 0:
                    self.status.append(1)
                else:
                    self.status.append(0)

            if sum (self.status) == number:
                self.bilangan_terkecil = i
                break
            else:
                self.status = list ()
                continue
            
        return self.bilangan_terkecil
    
if __name__ == "__main__":
    fg = bilangan()
    print fg.dapatkan_bilangan(10)

#===============================================
#nomor A5
def apakahPrima(x) :	        
    prim = True	                
    if x >= 2 :	                
        for i in range(2, x):	
            if x % i == 0 :	
                prim = False	
    else :	                
        prim = False	        
    return prim	                

##>>> apakahPrima(100)
##False
##>>>

##import time
##print time.strftime('%S')

'''5 DETIK'''
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

##print cariFaktorPrima(7824864274272489)
##print time.strftime('%S')
##[3, 2608288091424163]
##>>>

import time
current_milli_time = time.time()
##print current_milli_time

''' 4 DETIK '''
def factors(n):
    gaps = [1,2,2,4,2,4,2,4,6,10**9,10**9]
    length, cycle = 11, 10
    f, fs, next = 2, [], 0
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += gaps[next]
        next += 1
        if next == length:
            next = cycle
    if n > 1: fs.append(n)
    return fs

awal = time.time()
print factors(7824864274272489)
ahir = time.time()
print 'total', ahir - awal

##current_milli_time = int(round(time.time() * 1000))
##print current_milli_time
##print time.strftime('%S')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


