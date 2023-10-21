import tkinter as tk
from tkinter import messagebox

def Konversi():
    fahrenheit = float(entry_suhu.get())
    celsius = (fahrenheit - 32) * 5/9
    label_suhubaru = tk.Label(root, text=f"Hasil konversi suhunya : {celsius} derajat celcius")
    label_suhubaru.pack(padx=10, expand= True, fill="x", pady=10)

root = tk.Tk()
root.title("Konversi Suhu")
root.geometry("500x200")

label_suhu = tk.Label(root, text="Masukkan suhu (fahrenheit):")
label_suhu.pack(padx=10, expand= True, fill="x", pady=10)

entry_suhu = tk.Entry(root)
entry_suhu.pack(padx=10, expand= True, fill="x", pady=10)

btn_konversi = tk.Button(root, text="konversi", command=Konversi)
btn_konversi.pack(padx=5, expand= True, fill="x", pady=5)

root.mainloop()
