print ("------------------------")
print ("Nama : Dyea Puspita Sari")
print ("NIM  : 2409116084")
print ("------------------------")

# Masukan Nama Dan Pin

while True:
    print("Halo Selamat Datang Dhymarket")
    Nama = input("masukan nama: ")
    Pin = input("masukan pin: ")
    if Nama == "celly" and Pin == "123":
        print("Anda berhasil masuk di Dhymarket")
        break
    else:
        print("Anda Gagal Masuk Ke Dhymarket Silahkan Masukan Nama Dan Pin Dengan Benar")

while True:
    harga = int(input('Masukkan harga barang: '))
    jumlah = int(input('Masukkan jumlah barang: '))

    total_harga = harga * jumlah

    
    if harga > 250000:
        diskon = harga * 25/100
        total = harga - diskon
        print('=== Anda mendapatkan diskon sebesar 25% ===')
    elif harga < 250000:
        total = harga
        print('=== Anda tidak mendapatkan diskon ===  ')
    else:
        print('Anda tidak mendapatkan diskon')
        
    print('Total harga yang harus dibayar : ')

    lanjut = input('Apakah anda ingin menghitung total harga lagi? (y/n) : ')
    if lanjut.lower() != 'y' :
        print('Terimakasih!!!!')
        break