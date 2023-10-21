import sqlite3

def create_table():
    conn = sqlite3.connect("database_resto.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS menu (id_menu INTEGER not null PRIMARY KEY, nama_menu TEXT not null, harga_menu REAL not null, deskripsi_menu TEXT not null)")
    conn.commit()
    conn.close()


def insert(id_menu, nama_menu, harga_menu, deskripsi_menu):
    conn = sqlite3.connect("database_resto.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO list_bola (id_menu, nama_menu, harga_menu, deskripsi_menu) VALUES(?,?,?,?)", (id_menu, nama_menu, harga_menu, deskripsi_menu))
    conn.commit()
    conn.close()


def select_all():
    conn = sqlite3.connect("database_resto.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu")
    result = cursor.fetchall()
    conn.close()
    for record in result:
        print(record)


def update_jumlahBola_on_id(id, nama_menu):
    conn = sqlite3.connect("database_resto.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE menu SET nama_menu={nama_menu} WHERE id={id}")
    conn.commit()
    conn.close()


def delete_by_id(id):
    conn = sqlite3.connect("futsal_ku.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM list_bola WHERE id={id}")
    conn.commit()
    conn.close()


def search_name(keyword):
    conn = sqlite3.connect("futsal_ku.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM list_bola WHERE nama_penyewa LIKE '%{keyword}%'")
    result = cursor.fetchall()
    conn.close()
    for record in result:
        print(record)


print("=====TOKO ONLINE RINA=====")
while True:
    print(
        """Pilih menu:
    1. Create table
    2. Insert data
    3. Select all
    4. Update Description
    5. Delete by id
    6. Search name
    0. Exit
    """
    )

    opt = int(input("Pilih menu yang Anda inginkan (0/1/2/3/4/5/6): "))
    match opt:
        case 1:
            create_table()
            print("tabel berhasil dibuat!")
        case 2:
            id = input("Masukkan id: ")
            nama_penyewa = input("Masukkan nama penyewa: ")
            jumlah_bola = input("Masukkan jumlah bola: ")
            harga_total = float(input("Masukkan harga: "))
            insert(
                id=id,
                name=nama_penyewa,
                jumlah_bola=jumlah_bola,
                harga_total=harga_total,
            )
            print("Data berhasil dimasukkan!")
        case 3:
            print("List item: ")
            print(select_all())
        case 4:
            id = input("Masukkan id barang yang ingin diupdate: ")
            jumlah_bola = input("Masukkan jumlah bola yang baru: ")
            update_jumlahBola_on_id(id=id, jumlah_bola=jumlah_bola)
            print("Data berhasil diupdate!")
            if jumlah_bola >= 12:
                hargaDiskon = harga_total-0.1*harga_total
                print(f"Selamat Anda mendapat diskon dengan total harga diskon {hargaDiskon}")
            else:
                print("TIDAK ADA DISKON.")
        case 5:
            id = int(input("Masukkan id item yang ingin dihapus: "))
            delete_by_id(id=id)
            print(f"Data dengan id {id} berhasil dihapus!")
        case 6:
            keyword = input("Masukkan keyword item yang ingin dicari: ")
            print("Hasil search: ")
            print(search_name(keyword=keyword))
        case 0:
            print("Program selesai dijalankan...")
            break
        case _:
            continue