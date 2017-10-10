
def sortNIM(data):
  return sorted(data, key=lambda i: i['NIM'], reverse=False)  # Mengurutkan `data` berdasarkan `all_nim`

data = [
  {'NIM': 'L201', 'Nama': 'Ade'},
  {'NIM': 'L103', 'Nama': 'Namnung'},
  {'NIM': 'L203', 'Nama': 'Budi'},
  {'NIM': 'L110', 'Nama': 'Anduk'}
]
print data, '\n'
print sortNIM(data)
