# Nama File: is_kabisat.py
# Pembuat : Athallah Nazif Arlis Pratama
# Tanggal : 07 Oktober 2026
# Deskripsi : Fungsi yang menerima input x sebagai tahun dan mengembalikannilai true jika x % 400 == 0 or (x % 4 == 0 and x % 100 !=0)
# Definisi dan spesifikasi : 
#  is_kabisat(x): int -> bool
#   {is_kabisat(x) akan bernilai true jika x % 400 == 0 or (x % 4 == 0 and x % 100 != 0)}

def iskabisat(x:int) -> bool:
    return(x % 400 == 0 or (x % 4 == 0 and x % 100 != 0))

print(iskabisat(1900))
print(iskabisat(2000))
print(iskabisat(1996))