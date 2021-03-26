#Program mendaftar kursus online
print("""SELAMAT DATANG DI LAMAN PENDAFTARAN
        KURSUS ONLINE
LENGKAPI DATA BERIKUT UNTUK MELANJUTKAN""")
print("""
========================================
""")

Question1 = int(input('Berapakah usia kamu?'))
if Question1 < 21:
    print(" ")
    print('Maaf, Anda belum dapat mendaftar kursus ini')
else:
    Question2 = input('Apakah anda lulus ujian kualifikasi? (y/t) :')
    if Question2 == 'y':
        print(" ")
        print('Selamat, Anda dapat mendaftar di kursus ini')
    elif Question2 == 't':
        print(" ")
        print('Maaf, Anda belum dapat mendaftar di kursus ini')
    else:
        print("""INVALID CODE
            KODE YANG ANDA MASUKKAN TIDAK VALID""")
    print('''TERIMA KASIH TELAH PERCAYA PADA KAMI
    >>>>>>>><<<<<<<<>>>>>>>><<<<<<<<''')