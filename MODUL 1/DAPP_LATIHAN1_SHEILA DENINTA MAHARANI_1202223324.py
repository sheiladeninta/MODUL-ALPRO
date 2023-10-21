
def tambahDataWarga():
    namaWarga = input("Masukkan nama warga: ")
    alamatWarga = input("Masukkan alamat warga: ")
    dataWarga[namaWarga]=alamatWarga
    print("Data warga telah ditambahkan\n")

def cekNamaWarga():
    namaWarga = input("Masukkan nama warga: ")
    print("Warga tersebut beralamat di",dataWarga[namaWarga], "\n")

def hapusDataWarga():
    namaWarga = input("Masukkan nama warga: ")
    dataWarga.pop(namaWarga)
    print("Data warga tersebut telah dihapus\n")

dataWarga = {}

while True:
    print("""
    Menu:
    1. Tambahkan Nama Warga
    2. Mengecek Nama Warga
    3. Menghapus Nama Warga
    0. Exit
    """)
    pilihMenu = int(input("Masukkan nomor menu yang Anda inginkan: "))

    if pilihMenu == 1:
        tambahDataWarga()

    elif pilihMenu == 2:
        cekNamaWarga()

    elif pilihMenu == 3:
        hapusDataWarga()

    elif pilihMenu == 0:
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Menu tidak tersedia, silakan pilih menu yang lain")