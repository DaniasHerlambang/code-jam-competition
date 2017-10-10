from fractions import gcd
from functools import reduce

def sebuahFungsi(n):
  def lcm(x, y):
    # mengembalikan nilai dari `x*y` yang dibagi dengan pembagian bulat kebawah
    # dengan Faktor Persekutuan Terbesar/Greatest Common Divisor (GCD) dari `x` dan `y`.
    return x*y // gcd(x, y)

  # memastikan bahwa nilai `n` merupakan bilangan bulat positif.
  if n > 0:
    # mengembalikan nilai dari fungsi `lcm` dengan menggunakan module `reduce`
    return reduce(lcm, range(1, n+1))
  return False

##print sebuahFungsi(-2) #false
##print sebuahFungsi(0)  #false
##print sebuahFungsi(1)  #1
##print sebuahFungsi(5)  #60
##print sebuahFungsi(10) #2520
