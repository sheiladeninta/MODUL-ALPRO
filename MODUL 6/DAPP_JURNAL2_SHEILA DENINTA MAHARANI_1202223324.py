import matplotlib.pyplot as plt

satu = [20,17, 14]
dua = [27]
tiga = [3]
empat = [4]
lima = [5]
enam = [6]

fig, ax =plt.subplots(figsize=(10,10))

ax.set_xticklabels(['1 orang', '2 orang', '3 orang', '4 orang', '5 orang', '6 orang'])
ax.set_yticklabels(['y', '20 bungkus', '40 bungkus', '60 bungkus', '80 bungkus', '100 bungkus'])

plt.title("persebaran data dan rata-rata output produksi tiap jumlah tenaga kerja")
plt.boxplot((jumlahTK, output), meanline=True, showmeans=True)

plt.grid()
plt.show()

""" pada boxplot di atas, untuk data yang terkait memilki informasi meansline oranye, dan showmeans hijau"""