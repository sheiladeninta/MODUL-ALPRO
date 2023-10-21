import numpy as np

print("Selamat Datang di Lab Daspro\n")

umurPekerja = [29, 34, 38, 39, 42, 27, 41, 40, 33, 43]
jumlahPenjualan = [112, 99, 140, 139, 120, 110, 128, 134, 115, 164]

print("| Hubungan Variabel Umur dan Penjualan |\n")
korelasi = np.corrcoef(umurPekerja, jumlahPenjualan)[0][1]
print(f"Nilai koefisien korelasi : {korelasi}\n")
print("----> Kesimpulan <----")
if 0 <= korelasi < 0.199:
    print("Korelasi positif sangat rendah")
elif 0.199 <= korelasi <0.399:
    print("Korelasi positif rendah")
elif 0.399 <= korelasi <0.599:
    print("Korelasi positif sedang")
elif 0.599 <= korelasi <0.799:
    print("Korelasi positif kuat")
elif 0.799 <= korelasi <1:
    print("Korelasi positif sangat kuat")
elif -0.199 < korelasi <=0:
    print("Korelasi negatif sangat rendah")
elif -0.399 < korelasi <=-0.199:
    print("Korelasi negatif rendah")
elif -0.599 < korelasi <= -0.399:
    print("Korelasi negatif sedang")
elif -0.799 < korelasi <= -0.599:
    print("Korelasi negatif kuat")
elif -1 < korelasi <= -0.799:
    print("Korelasi negatif sangat kuat")
else :
    print("tidak valid")
