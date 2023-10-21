import matplotlib.pyplot as plt

A = [100, 135, 45, 135, 95, 80, 110, 115, 85, 40]
B = [115, 45, 50, 35, 160, 80, 140, 130, 85, 95]
C = [85, 55, 135, 140, 170, 75, 40, 140, 50, 55]

AVBVC = A + B + C

syaratLomba = [data for data in AVBVC if 60 <= data <= 120]

plt.hist(syaratLomba, color='blue', bins=range(60,121,10), edgecolor="black", label="Berat Badan Ideal")

plt.xticks(range(60,121,10))
plt.title("Data Berat Badan Mahasiswa DasPro")
plt.xlabel("Berat Badan")
plt.ylabel("Frekuensi")

plt.legend()
plt.show()

"""Berdasarkan histogram yang ditampilkan, dapat disimpulkan bahwa data berat badan yang ideal paling banyak berada di rentang berat badan 80-90 dengan jumlah 5 data"""