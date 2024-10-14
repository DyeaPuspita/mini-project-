from getpass import os
from prettytable import PrettyTable

print('''
+==================================================================================================+
|                  SISTEM PERBAIKAN AKUN YANG TERSESI ATAU TERBLOKIR                               |
+==================================================================================================+
''')

# Data login untuk admin user
nama_admin = "pengguna"
admin_password = "cecaa12"

print('Akun yang tersesi')
penyewaan = input('Masukkan nama penyewa: ')

total1 = 0
jenis1 = ''
total2 = 0
jenis2 = ''

def fungsiaplikasi():
    global total1
    global jenis1
    print('\n----------------Jenis aplikasi--------------')
    print('1. Facebook = Rp 500000')
    print('2. Instagram = Rp 200000')
    print('3. Tiktok = Rp 9000000')
    print('4. Email = Rp 100000')
    
    nomor = int(input('Masukkan pilihan aplikasi (1, 2, 3, dan 4): '))
    hari = int(input('Berapa hari: '))

    if nomor == 1:
        total1 = hari * 500000
        jenis1 = 'Facebook'
    elif nomor == 2:
        total1 = hari * 200000
        jenis1 = 'Instagram'
    elif nomor == 3:
        total1 = hari * 9000000
        jenis1 = 'Tiktok'
    elif nomor == 4:
        total1 = hari * 100000
        jenis1 = 'Email'
    else:
        print('Pilihan tidak ada, silahkan masukkan lagi!!')
        return fungsiaplikasi()  # Memanggil kembali jika salah input
    
    print(f'Biaya perbaikan_akun {jenis1} = Rp {total1}')

def fungsiUser():
    global total2
    global jenis2
    print('\n--------------Customer-------------')
    print('1. Facebook ---> Rp 500000 per hari')
    print('2. Instagram ---> Rp 200000 per hari')
    print('3. Tiktok ---> Rp 9000000 per hari')
    print('4. Email ---> Rp 100000 per hari')

    nomor = int(input('Masukkan pilihan customer: '))

    if nomor == 1:
        total2 = 500000
        jenis2 = 'Facebook'
    elif nomor == 2:
        total2 = 200000
        jenis2 = 'Instagram'
    elif nomor == 3:
        total2 = 9000000
        jenis2 = 'Tiktok'
    elif nomor == 4:
        total2 = 100000
        jenis2 = 'Email'
    else:
        print('Pilihan tidak ada, silahkan masukkan lagi!!')
        return fungsiUser()  # Memanggil kembali jika salah input

    print(f'Biaya penyewaan {jenis2} per-hari = Rp {total2}')

# Panggil fungsi untuk memilih alat dan customer()
fungsiaplikasi()
fungsiUser()

# Untuk menghitung total semua
totalsemua = total1 + total2

# Untuk menghitung kembalian
jumlah_uang = int(input('Jumlah uang yang diberikan: Rp '))
kembalian = jumlah_uang - totalsemua

# Mencetak struk menggunakan PrettyTable
print('\n=================== S T R U K  PENYEWAAN JASA PERBAIKAN AKUN =======================')
tabel = PrettyTable()
tabel.field_names = ["Nama Aplikasi", "Tagihan", "Jumlah Uang", "Kembalian"]

# Menambahkan baris ke tabel
tabel.add_row([penyewaan, f"Rp {totalsemua}", f"Rp {jumlah_uang}", f"Rp {kembalian}"])

print(tabel)
print('=======================Terimakasih==============================')