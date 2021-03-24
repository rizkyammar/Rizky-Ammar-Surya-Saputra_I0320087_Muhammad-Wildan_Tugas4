#Mengimplementasikan program menggunakan operator floor
print("""MENGHITUNG HASIL PEMBAGIAN BILANGAN BULAT
DENGAN MENGABAIKAN HASIL KOMANYA
MENGGUNAKAN OPERATOR FLOOR

======================================================""")

print("""
""")

question = input('Apakah anda ingin menjalankan program ini?(y/n): ')

if question == 'y':
    print('Masukkan nilai yang ingin anda hitung!')
    a = float(input('Masukkan Bilangan bulat pertama: '))
    b = float(input('Masukkan Bilangan bulat kedua:'))
    print('Maka hasilnya adalah =', a//b)


elif question == 'n':
    print('Terima kasih telah membuka program ini')

else:
    print("""INVALID CODE
    KODE YANG ANDA MASUKKANN TIDAK TERDAFTAR""")

print("""TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI
>>>>>>>>>><<<<<<<<<<>>>>>>>>>><<<<<<<<<<""")