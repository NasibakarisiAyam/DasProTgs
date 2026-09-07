# Nama File: menghitung_total_diskkon.py
# Pembuat : Athallah Nazif Arlis Pratama
# Tanggal : 07 Oktober 2026
# Deskripsi : Fungsi yang menerima input a:int sebagai harga dan b:int sebagai harga dan akan mengembalikan 
# nilai dari (a-(a*(b/100))) 
# yang menghasilkan nilai float
# Definisi dan spesifikasi : 
#  total_diskon(a,b): int -> float
#   {total_diskon(a,b) akan mengembalikan nilai dari (a - (a*b/100))}
def total_diskon(a:int,b:int) -> float:
    return(a - (a*(b/100)))

print(total_diskon(100000,50))