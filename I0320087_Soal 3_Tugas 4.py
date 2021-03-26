#Menentukan kapasitas maksimum bagasi pesawat
print('Menentukan berat maksimal dibawa di bagasi maskapai')
print(' ')
print('============')

print('Berat maksimal yg dapat dibawa di bagasi = 50 lbs')
print('Dengan, 50 lbs = 22.6kg')
print(' ')
print("""1) 110 Kg
2) 49 Kg
3) jumlah lainnya""")
Question1 = int(input('Masukkan Berat Benda Dalam Kilogram: '))
m1 = 110
m2 = 49
if Question1 == 1:
    if m1 <= 22.6:
        print('TRUE')
    else:
        print('FALSE')

elif Question1 == 2:
    if m2 <= 22.6:
        print('TRUE')
    else:
        print('FALSE')

elif Question1 == 3:
    c = int(input('Masukkan Berat Barang Total:'))
    if c <= 22.6:
        print('TRUE')
    else:
        print('FALSE')

else:
    print("""INVALID CODE
    KODE YANG ANDA MASUKKAN TIDAK TERDAFTAR""")