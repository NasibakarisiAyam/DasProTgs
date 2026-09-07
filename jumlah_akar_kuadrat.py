# Nama File: jumlah_akar.py
# Pembuat : Athallah Nazif Arlis Pratama
# Tanggal : 07 Oktober 2026
# Deskripsi : Fungsi yang menerima 4 input integer dan akan mengembalikan nilai dari jumlah akar-akar kuadrat
# Definisi dan spesifikasi : 
#  jumlah_akar(a,b,c): int -> float
#   {jumlah_akar(a,b,c) akan menerima input 4 bilangan dan akan mengembalikan nilai dari -b +/- (b^2-4ac)**0.5/2a yang dijumlahkan}

def jumlah_akar(a:int,b:int,c:int) -> float:
    
    return (((-b/a)**2) - (2*(c/a)))

print(jumlah_akar(1,6,9))