# CARA 1
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






# CARA 2
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
