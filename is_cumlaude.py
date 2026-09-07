# Nama File: is_cumlaude.py
# Pembuat : Athallah Nazif Arlis Pratama
# Tanggal : 07 Oktober 2026
# Deskripsi : Fungsi yang menerima input a:float dan b:float dan mengembalikan nilai true jika ipk >= 3.0 and waktu <= 54 
# Definisi dan spesifikasi : 
#  is_cumlaude(x,waktu): float -> bool
#   {is_cumlaude(x,y) akan menerima input float dan akan bernilai true jika ipk >= 3.50 and  waktu <= 54}

def iscumlaude(ipk:float, waktu:float)-> bool:
    return(ipk >= 3.50 and waktu <= 54)

print(iscumlaude(3.90,54))