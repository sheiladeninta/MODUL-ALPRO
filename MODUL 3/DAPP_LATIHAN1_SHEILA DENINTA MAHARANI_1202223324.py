import sqlite3

DATABASE_FILE = "DBA.sqlite3"

# Ubahlah semua value "pass" dari function-function dibawah dengan kode anda


def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS daftar_produk (id INTEGER not null PRIMARY KEY, name TEXT(100) not null, description TEXT(100) not null, price REAL not null)")
    conn.commit()
    conn.close()


def insert(id, name, description, price):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO daftar_produk (id, name, description, price) VALUES(?,?,?,?)", (id, name, description, price))
    conn.commit()
    conn.close()


def select_all():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM daftar_produk")
    result = cursor.fetchall()
    conn.close()
    for record in result:
        print(record)


def update_description_on_id(id, description):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE daftar_produk SET description={description} WHERE id={id}")
    conn.commit()
    conn.close()


def delete_by_id(id):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM daftar_produk WHERE id={id}")
    conn.commit()
    conn.close()


def search_name(keyword):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM daftar_produk WHERE name LIKE '%{keyword}%'")
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
            name = input("Masukkan nama material: ")
            description = input("Masukkan deskripsi: ")
            price = float(input("Masukkan harga: "))
            insert(
                id=id,
                name=name,
                description=description,
                price=price,
            )
            print("Data berhasil dimasukkan!")
        case 3:
            print("List item: ")
            print(select_all())
        case 4:
            id = input("Masukkan id barang yang ingin diupdate: ")
            description = input("Masukkan description yang baru: ")
            update_description_on_id(id=id, description=description)
            print("Data berhasil diupdate!")
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