import matplotlib.pyplot as plt

jumlahTK = [5,4,6,1,2,5,4,3,2,1,2,2,3,4,5,6,1,2,3,4]
output = [100,64,116,20,35,98,54,45,27,17,25,24,48,73,87,103,14,29,47,78]

fig, ax = plt.subplots(figsize=(7,6))

ax.set_xticklabels(['0','1 orang', '2 orang', '3 orang', '4 orang', '5 orang', '6 orang'])
ax.set_yticklabels(['0', '20 bungkus', '40 bungkus', '60 bungkus', '80 bungkus', '100 bungkus'])

plt.scatter(jumlahTK,output, color='black', marker='o', s = 20)

plt.xlabel("Jumlah Tenaga Kerja")
plt.ylabel("Hasil Produksi")
plt.title("Hubungan antara Jumlah Tenaga Kerja dan Jumlah Produk yang Dihasilkan")

plt.grid()
plt.show()