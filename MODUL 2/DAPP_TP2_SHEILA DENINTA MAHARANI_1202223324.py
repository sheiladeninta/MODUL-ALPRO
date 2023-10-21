# Nama : Sheila Deninta Maharani
# Kelas : SI-46-08
# NIM : 1202223324
class Produk:
    def __init__(self, kode, nama, harga, stok):
        self.kode_produk = kode
        self.nama_produk = nama
        self.harga_produk = harga
        self.stok_produk = stok

class TokoOnline:
    def __init__(self):
        self.daftar_produk = []
    
    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
        print("Produk berhasil ditambahkan!")
    
    def tampilkan_produk(self):
        if not self.daftar_produk:
            print("Belum ada produk")
        else:
            print("Daftar Produk:")
            for produk in self.daftar_produk:
                print("Kode : {} | Nama : {} | Harga : {} | Stok : {}".format(
                    produk.kode_produk, produk.nama_produk, produk.harga_produk, produk.stok_produk))
    
    def hapus_produk(self, kode):
        for produk in self.daftar_produk:
            if produk.kode_produk == kode:
                self.daftar_produk.remove(produk)
                print("Produk berhasil dihapus!")
                break
        else:
            print("Produk tidak ditemukan!")
    
    def menu(self):
        while True:
            print("""
            ==== Toko Online ====
            1. Tambah Produk
            2. Daftar Produk
            3. Hapus Produk
            4. Keluar
            """)
            pilihMenu = input("Silakan pilih menu (1/2/3/4): ")
            
            if pilihMenu == "1":
                while True:
                    kode = input("Masukkan kode produk: ")
                    nama = input("Masukkan nama produk: ")
                    
                    while True:
                        try:
                            harga = int(input("Masukkan harga produk: "))
                            break
                        except ValueError:
                            print("Data yang diisi harus berupa bilangan bulat!")
                    
                    while True:
                        try:
                            stok = int(input("Masukkan stok produk: "))
                            break
                        except ValueError:
                            print("Data yang diisi harus berupa bilangan bulat!")
                    
                    produk = Produk(kode, nama, harga, stok)
                    self.tambah_produk(produk)
                    break
            
            elif pilihMenu == "2":
                self.tampilkan_produk()
            
            elif pilihMenu == "3":
                kode = input("Masukkan kode produk yang ingin dihapus: ")
                self.hapus_produk(kode)
            
            elif pilihMenu == "4":
                print("Terima kasih telah menggunakan aplikasi Toko Online!")
                break
            
            else:
                print("Invalid kode menu! Menu yang Anda pilih tidak tersedia, silakan pilih menu yang lain!")


toko = TokoOnline()
toko.menu()

