import numpy as np

nilai = []

n = int(input("Berapa banyak siswa dalam satu kelas?"))

for i in range(n):
    x = int(input("Masukkan nilai siswa ke-" + str(i+1) + ": "))
    nilai.append(x)

print("Menu:")
print("1. Menghitung nilai rata-rata kelas")
print("2. Menghitung nilai tertinggi di kelas")
print("3. Menampilkan jumlah siswa yang nilainya di bawah batas lulus")
print("4. Keluar")

while True:
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:
        print("Nilai rata-rata kelas adalah ", np.mean(nilai))
    elif pilihan == 2:
        print("Nilai tertinggi di kelas adalah ", np.max(nilai))
    # elif pilihan == 3:
    # if nilai < 70:
    #     print("Jumlah siswa yang nilainya di bawah batas lulus adalah",)
    elif pilihan == 4:
        print("Thank you")
        return
    else:
        print("Pilihan tidak valid")
        break