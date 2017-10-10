def checkUnic(inputString):
  for i in inputString:
    #Proses dimana jumlah karakter di hitung apakah karakter tersebut memliliki duplicate/tidak.
    if inputString.count(i) > 1:
      return False
  return True

print checkUnic('Jakarta')
print checkUnic('Jaktu')

