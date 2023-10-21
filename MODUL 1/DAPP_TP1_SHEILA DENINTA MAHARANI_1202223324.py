print("====PROGRAM MANAJEMEN DATA PENDAPATAN PENJUALAN NASI GORENG KATSU====\n")

namaPemilik = input("Masukkan nama Anda: ")
print("\n==========Selamat Datang di Program ini, " + namaPemilik + "!==========")

def tambahDataPendapatan():
    jumlah = int(input("Masukkan data pendapatan: "))
    dataPendapatan.append(jumlah)
    print(f"Data pendapatan penjualan nasi goreng katsu sebesar Rp{jumlah} berhasil ditambahkan\n")

def urutanDataPendapatan():
    dataPendapatan.sort(reverse=True)
    print("Data pendapatan penjualan nasi goreng katsu berhasil diurutkan\n")

def totalPendapatan():
    total = sum(dataPendapatan)
    print(f"Total pendapatan penjualan nasi goreng katsu adalah Rp {total}\n")

def hapusDataPendapatan():
    if len(dataPendapatan) == 0:
        print("Belum ada data pendapatan. Coba tambah data terlebih dahulu!")
    else:
        tampilanDataPendapatan()
        nominal_pendapatan = int(input("Masukkan pendapatan yang ingin dihapus: "))
        if nominal_pendapatan in dataPendapatan:
            dataPendapatan.remove(nominal_pendapatan)
            print(f"Data pendapatan penjualan nasi goreng katsu sebesar Rp{nominal_pendapatan} berhasil dihapus\n")
        else:
            print(f"Data pendapatan penjualan nasi goreng katsu sebesar Rp{nominal_pendapatan} tidak ditemukan\n")

def tampilanDataPendapatan():
    if len(dataPendapatan) == 0:
        print("Belum ada data pendapatan. Coba tambah data terlebih dahulu!")
    else:
        print("Data pendapatan penjualan nasi goreng katsu:")
        for i, pendapatan in enumerate(dataPendapatan):
            print(f"{i+1}. Rp {pendapatan}")

dataPendapatan = []

while True:
    print("""
    Menu:
    1. Tambahkan Data Pendapatan
    2. Mengurutkan Total Data dari yang Terbesar
    3. Menghitung Total Data Pendapatan
    4. Menghapus Data Pendapatan
    5. Menampilkan Seluruh Data Pendapatan
    0. Exit
    """)
    pilihMenu = int(input("Masukkan nomor menu yang Anda inginkan: "))

    if pilihMenu == 1:
        tambahDataPendapatan()

    elif pilihMenu == 2:
        urutanDataPendapatan()

    elif pilihMenu == 3:
        totalPendapatan()

    elif pilihMenu == 4:
        hapusDataPendapatan()

    elif pilihMenu == 5:
        tampilanDataPendapatan()

    elif pilihMenu == 0:
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Menu tidak tersedia, silakan pilih menu yang lain")
