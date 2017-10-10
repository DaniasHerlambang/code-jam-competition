'''Tab indentation: 2'''

def checkPossibleOrder(n): 
    x = 6
    y = 9
    z = 20
    possible = False

    if (n < x):                                         #memastikan bahwa nilai `n` tidak kurang dari minimum possible order, yaitu `x`.
        return False
    if ((n % x == 0) or (n % y == 0) or (n % z == 0)):  #mencheck apakah `n` habis ketika dimodulus oleh salah satu dari possible order yaitu: `x, y & z`
        return True
    if (possible == False and n > x):                   #jika nilai dari `possible` masih tetap `False` dan jika nilai `n` lebih dari `x`
        possible = checkPossibleOrder(n - x)            #selanjutnya dilakukan pengecekan lagi, dimana nilai `n` dikurang dengan `x`.
    if (possible == False and n > y):                   #begitu juga pada proses pengecekan selanjutnya.
        possible = checkPossibleOrder(n - y)
    if (possible == False and n > z):
        possible = checkPossibleOrder(n - z)
    return possible

print checkPossibleOrder(-6) #false
print checkPossibleOrder(-2) #false
print checkPossibleOrder(3)  #false
print checkPossibleOrder(6)  #true
print checkPossibleOrder(9)  #true
print checkPossibleOrder(12) #true
print checkPossibleOrder(15) #true
print checkPossibleOrder(18) #true
print checkPossibleOrder(20) #true
print checkPossibleOrder(35) #true
print checkPossibleOrder(13) #false
print checkPossibleOrder(70) #true
