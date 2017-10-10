
# CARA 1
def sebuahFungsi(n, mul_1, mul_2):
  out_list = []
  for i in range(1, n):                           # mengiterasi `n`, yang dimulai dari `1`->`n`, ex: [1, 2, 3, 4, ..., 9]
    if ((i % mul_1) == 0 or ( i % mul_2) == 0):   # mengecek apakah `i` merupakan bilangan yang habis dibagi ke-2 kelipatan.
      out_list.append(i)                          # jika kondisi diatas terpenuhi, selanjutnya menambahkan nilai `i` tersebut kedalam `out_list`.
  return sum(out_list)                            # menjumlahkan seluruh angka yang ada di `out_list`

print sebuahFungsi(10, 3, 5) #23



# CARA 2, menggunakan lambda.
# Metode ini lebih simple dari dari metode sebelumnya, dengan memanfaatkan list comprehension.
sebuahFungsi = lambda n, mul_1, mul_2: sum([ i for i in range(1, n) if i % mul_1 == 0 or i % mul_2 == 0 ])

print sebuahFungsi(10, 3, 5)
