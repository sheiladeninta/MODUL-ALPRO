import sqlite3

def create_table():
    conn = sqlite3.connect("DBA.sqlite3.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER not null PRIMARY KEY, item_name TEXT not null, description TEXT, damage INTEGER, durability REAL)")
    conn.commit()
    conn.close()


def drop_table():
    conn = sqlite3.connect("DBA.sqlite3.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE items")
    conn.commit()
    conn.close()


def insert(id, item_name, description, damage, durability):
    conn = sqlite3.connect("DBA.sqlite3.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (id, item_name, description, damage, durability) VALUES(?,?,?,?,?)", (id, item_name, description, damage, durability))
    conn.commit()
    conn.close()


def select_all():
    conn = sqlite3.connect("DBA.sqlite3.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    result = cursor.fetchall()
    conn.close()
    for record in result:
        print(record)


def select_column(column_name):
    conn = sqlite3.connect("DBA.sqlite3.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT DISTINCT {column_name} FROM items")
    result = cursor.fetchall()
    conn.close()
    for record in result:
        print(record)


def update_durability_on_id(id, durability):
    conn = sqlite3.connect("DBA.sqlite3.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE items SET durability={durability} WHERE id={id}")
    conn.commit()
    conn.close()


def delete_by_id(id):
    conn = sqlite3.connect("DBA.sqlite3.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM items WHERE id={id}")
    conn.commit()
    conn.close()


def search_name(keyword):
    conn = sqlite3.connect("DBA.sqlite3.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM items WHERE item_name LIKE '%{keyword}%'")
    result = cursor.fetchall()
    conn.close()
    for record in result:
        print(record)


print("=====DASPRO BIZZARE ADVENTURE=====")
while True:
    print("""
    Menu:
    1. Create table
    2. Insert data
    3. Select all
    4. Select column
    5. Update durability
    6. Delete by id
    7. Search name
    8. Drop table
    0. Exit
    """
    )

    while True:
        try:
            opt = int(input("Pilih menu yang Anda inginkan (0/1/2/3/4/5/6/7/8): "))
            break
        except ValueError:
            print("input yang Anda masukkan tidak valid! inputan harus berupa data integer")
    match opt:
        case 1:
            create_table()
            print("tabel berhasil dibuat!")
        case 2:
            id = input("Masukkan id: ")
            item_name = input("Masukkan nama item: ")
            description = input("Masukkan deskripsi item: ")
            while True:
                try:
                    damage = int(input("Masukkan damage item: "))
                    break
                except ValueError:
                    print("input yang Anda masukkan tidak valid! inputan harus berupa data integer")
            while True:
                try:
                    durability = float(input("Masukkan durability item: "))
                    break
                except ValueError:
                    print("input yang Anda masukkan tidak valid! inputan harus berupa data float")
            insert(
                id=id,
                item_name=item_name,
                description=description,
                damage=damage,
                durability=durability,
            )
            print("Data berhasil dimasukkan!")
        case 3:
            print("List item: ")
            print(select_all())
        case 4:
            column_name = input("Masukkan nama kolom: ")
            print(f"list data pada kolom {column_name}: ")
            print(select_column(column_name=column_name))
        case 5:
            id = input("Masukkan id barang yang ingin diupdate: ")
            durability = input("Masukkan durability item yang baru: ")
            update_durability_on_id(id=id, durability=durability)
            print("Data berhasil diupdate!")
        case 6:
            id = int(input("Masukkan id item yang ingin dihapus: "))
            delete_by_id(id=id)
            print(f"Data dengan id {id} berhasil dihapus!")
        case 7:
            keyword = input("Masukkan keyword item yang ingin dicari: ")
            print("Hasil search: ")
            print(search_name(keyword=keyword))
        case 8:
            confirm = input("Apakah anda yakin? (y/n): ")
            if confirm == "y":
                drop_table()
                print("tabel berhasil didrop!")
            elif confirm == "n":
                print("tabel tidak jadi didrop!")
            else:
                print("input yang Anda masukkan tidak valid! pilihlah 'y' untuk 'yes' atau 'n' untuk 'no'")
                continue
        case 0:
            print("Program selesai dijalankan...")
            break
        case _:
            continue