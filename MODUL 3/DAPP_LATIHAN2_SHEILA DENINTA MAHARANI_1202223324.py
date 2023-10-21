import sqlite3 as sq


def clearTable():  # dibiarkan saja
    conn = sq.connect("database_toko.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM inventory")
    conn.commit()
    conn.close()


def CreateTable():
    conn = sq.connect("database_toko.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inventory (id INTEGER not null PRIMARY KEY, name TEXT not null, price REAL not null, quantity INTEGER not null, description TEXT not null)")
    conn.commit()
    conn.close()


def add_item(id, name, price, quantity, description):
    conn = sq.connect("database_toko.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO inventory (id, name, price, quantity, description) VALUES(?,?,?,?,?)", (id, name, price, quantity, description))
    conn.commit()
    conn.close()


def remove_item(id):
    conn = sq.connect("database_toko.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM inventory WHERE id={id}")
    result = cur.fetchall()
    return result


def update_item(id, name, price, quantity, description):
    conn = sq.connect()
    cur = conn.cursor()
    cur.execute(f"UPDATE inventory SET name='{name}', price='{price}', quantity={quantity} WHERE id='{id}'")
    conn.commit()
    conn.close()


print("""
      ======= APLIKASI MANAJEMEN INVESTARIS TOKO =======
      1. Menambah Item
      2. Menghapus Item
      3. Mengubah Item
      0. Exit
      """)

clearTable()
CreateTable()

while True:
    input_aplikasi = int(input("Masukkan menu: "))
    if input_aplikasi == 1:
        input_id = int(input("item's ID: "))
        input_name = input("item's name: ")
        input_price = int(input("item's price: "))
        input_quantity = int(input("item's quantity: "))
        input_desc = input("item's desc: ")
        add_item(input_id=id, input_name=name, input_price=price, input_quantity=quantity, input_desc=description)
        print("data berhasil ditambahkan!")
    elif input_aplikasi == 2:
        input_keyword = input("keyword: ")
        remove_item(input_keyword=id)
        print(f"data {input_keyword} berhasil dihapus!")
    elif input_aplikasi == 3:
        input_id = int(input("ID item yang ingin dirubah: "))
        input_NewName = input("new name: ")
        input_NewPrice = int(input("new price: "))
        input_NewQuantity = int(input("new quantity: "))
        input_NewDesc = input("new desc: ")
        update_item(input_id=id, input_NewName=name, input_NewPrice=price,
                    input_NewQuantity=quantity, input_NewDesc=description)

    elif input_aplikasi == 0:
        break
    else:
        print("Invalid input")