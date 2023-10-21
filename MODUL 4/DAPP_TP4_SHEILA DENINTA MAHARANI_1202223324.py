import sqlite3
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class Tampilan:
    namaDB = "CRUDmahasiswa.db"

    def __init__(self, root):
        self.root = root
        self.root.title("Program CRUD Mahasiswa")
        self.root.configure(background='#008CBA')

        self.input_frame = ttk.LabelFrame(text="Input Data Mahasiswa")
        self.input_frame.pack(side=tk.LEFT, padx=20)

        self.NIM = ttk.Label(self.input_frame, text= "NIM :")
        self.NIM.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.NIM_entry = ttk.Entry(self.input_frame)
        self.NIM_entry.grid(row=0, column=1, padx=5, pady=5)

        self.nama = ttk.Label(self.input_frame, text= "Nama :")
        self.nama.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.nama_entry = ttk.Entry(self.input_frame)
        self.nama_entry.grid(row=1, column=1, padx=5, pady=5)

        self.alamat = ttk.Label(self.input_frame, text= "Alamat :")
        self.alamat.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.alamat_entry = ttk.Entry(self.input_frame)
        self.alamat_entry.grid(row=2, column=1, padx=5, pady=5)

        self.jurusan = ttk.Label(self.input_frame, text= "Jurusan :")
        self.jurusan.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.jurusan_entry = ttk.Entry(self.input_frame)
        self.jurusan_entry.grid(row=3, column=1, padx=5, pady=5)

        self.button_frame = ttk.Frame()
        self.button_frame.pack(side=tk.LEFT, padx=20)

        style = ttk.Style()
        style.configure('primary.TButton', foreground='#000000', background='#008CBA')
        style.configure('warning.TButton', foreground='#000000', background='#008CBA')
        style.configure('danger.TButton', foreground='#000000', background='#008CBA')

        self.add_button = ttk.Button(
            self.button_frame, text="Add", style='primary.TButton', command=self.add_data
        )
        self.add_button.pack(fill=tk.X, padx=5, pady=5)

        self.edit_button = ttk.Button(
            self.button_frame, text="Edit", style='warning.TButton', command=self.edit_data
        )
        self.edit_button.pack(fill=tk.X, padx=5, pady=5)

        self.delete_button = ttk.Button(
            self.button_frame, text="Delete", style='danger.TButton', command=self.delete_data
        )
        self.delete_button.pack(fill=tk.X, padx=5, pady=5)


        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        # Menambahkan style untuk baris pertama
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=1, bd=1,
                        font=('Calibri', 12), rowheight=25,
                        background='#E1F5FE', foreground='black',
                        fieldbackground='#F5F5F5')
        style.map("mystyle.Treeview", 
                background=[('selected', '#008CBA')],
                foreground=[('selected', 'white')])

        self.tree = ttk.Treeview(
            self.table_frame,
            columns=("NIM", "Nama", "Alamat", "Jurusan"),
            show="headings",
            style="mystyle.Treeview"
        )
        self.tree.heading("NIM", text="NIM")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Alamat", text="Alamat")
        self.tree.heading("Jurusan", text="Jurusan")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Memanggil fungsi untuk menampilkan data pada tabel
        self.create_table()
        self.show_data()

        def on_close():
            response=tkinter.messagebox.askyesno('Exit','Are you sure you want to exit?')
            if response:
                self.root.destroy()

        self.root.protocol('WM_DELETE_WINDOW', on_close)
    
    def run(self):
        self.root.mainloop()

    def execute_query(self, query, params=()):
        with sqlite3.connect(self.namaDB) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params)
            conn.commit()
        return result

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS mahasiswa (
            NIM INTEGER NOT NULL PRIMARY KEY,
            Nama TEXT NOT NULL,
            Alamat TEXT NOT NULL,
            Jurusan TEXT NOT NULL
            )"""
        self.execute_query(query=query)

    def show_data(self):
        records = self.tree.get_children()
        for record in records:
            self.tree.delete(record)

        query = "SELECT NIM, Nama, Alamat, Jurusan FROM mahasiswa"
        data = self.execute_query(query).fetchall()
        for row in data:
            self.tree.insert("", tk.END, values=row)

    def add_data(self):
        NIM = self.NIM_entry.get()
        nama = self.nama_entry.get()
        alamat = self.alamat_entry.get()
        jurusan = self.jurusan_entry.get()

        if NIM == "" or nama == "" or alamat == "" or jurusan == "":
            tkinter.messagebox.showerror("Error", "Mohon lengkapi semua input")
            return

        query = "SELECT * FROM mahasiswa WHERE NIM = ?"
        params = (NIM,)
        result = self.execute_query(query, params)

        if result.fetchone() is not None:
            tkinter.messagebox.showerror("Error", "NIM sudah terdaftar di database")
            return

        query = "INSERT INTO mahasiswa (NIM, Nama, Alamat, Jurusan) VALUES (?, ?, ?, ?)"
        params = (NIM, nama, alamat, jurusan)
        self.execute_query(query, params)

        self.NIM_entry.delete(0, tk.END)
        self.nama_entry.delete(0, tk.END)
        self.alamat_entry.delete(0, tk.END)
        self.jurusan_entry.delete(0, tk.END)

        self.show_data()

    def edit_data(self):
        NIM = self.NIM_entry.get()
        nama = self.nama_entry.get()
        alamat = self.alamat_entry.get()
        jurusan = self.jurusan_entry.get()

        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        id = values[0]

        if NIM == "" or nama == "" or alamat == "" or jurusan == "":
            tkinter.messagebox.showerror("Error", "Mohon lengkapi semua input")
            return

        query = "UPDATE mahasiswa SET NIM=?, Nama=?, Alamat=?, Jurusan=? WHERE NIM=?"
        params = (NIM, nama, alamat, jurusan, id)
        self.execute_query(query, params)

        self.show_data()
        self.clear_entries()

    def delete_data(self):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        id = values[0]

        query = "DELETE FROM mahasiswa WHERE NIM=?"
        params = (id,)
        self.execute_query(query, params)
        self.show_data()

    def clear_entries(self):
        self.NIM_entry.delete(0, tk.END)
        self.nama_entry.delete(0, tk.END)
        self.alamat_entry.delete(0, tk.END)
        self.jurusan_entry.delete(0, tk.END)

        self.show_data()

    def delete_data(self):
        if not self.tree.focus():
            tkinter.messagebox.showwarning(
                title="Warning", message="Please select data to delete"
            )
            return

        result = tkinter.messagebox.askquestion(
            title="Delete Confirmation", message="Are you sure to delete this data?"
        )
        if result == "yes":
            selected_item = self.tree.focus()
            NIM = self.tree.item(selected_item)["values"][0]
            query = f"DELETE FROM mahasiswa WHERE NIM = '{NIM}'"
            self.execute_query(query=query)

            self.show_data()

    
if __name__ == "__main__": 
    app = Tampilan(root=tk.Tk()) 
    app.root.mainloop()

