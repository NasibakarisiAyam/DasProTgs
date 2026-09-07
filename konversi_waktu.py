# Nama File: konversi_waktu
# Pembuat : Athallah Nazif Arlis Pratama
# Tanggal : 07 Oktober 2026
# Deskripsi : Fungsi yang mengkonversi waktu ke detik
# Definisi dan spesifikasi : 
#  konversi_waktu(jam,menit,detik): int -> int:
#   konversi_waktu(jam,menit,detik) akan memgembalikan nilai waktu dengan cara ((jam*3600) + (menit*60) + detik)


def konversi_waktu(jam:int,menit:int,detik:int)->int:
    return((jam*3600) + (menit*60)+detik)

print(konversi_waktu(1,30,0))