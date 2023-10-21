import sqlite3
import tkinter as tk

def tampilkan_buah():
    buah = var.get()
    label.config(text=f"Anda memilih {buah}")

root = tk.Tk()
root.title("Milih Buah")
root.geometry("300x200")

label_pilih = tk.Label(root, text="Anda memilih buah!")
label_pilih.pack(padx=10, expand= True, fill=tk.BOTH, pady=10)

var = tk.StringVar(root)
var.set("pilih buah")
namaBuah = ["pisang", "apel", "mangga"]
dropdown = tk.OptionMenu(root, var, *namaBuah)
dropdown.pack(padx=10, expand= True, fill=tk.BOTH, pady=10)

btn_tampilkan = tk.Button(root, text="Tampilkan", command=tampilkan_buah)
btn_tampilkan.pack(padx=5, expand= True, fill="x", pady=5)
root.mainloop()