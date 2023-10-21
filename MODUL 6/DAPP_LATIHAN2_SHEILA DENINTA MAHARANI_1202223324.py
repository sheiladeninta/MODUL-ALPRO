import matplotlib.pyplot as plt

tahun = [2013, 2014 ,2015 ,2016 ,2017 ,2018 ,2019 ,2020 ,2021 ,2022]

Bandung = [80000, 55000, 65000, 50000, 70000, 65000, 90000, 85000, 60000, 75000]
Subang = [42000, 64000, 36000, 50000, 72000,  47000, 58000, 88000, 86000, 74000 ]

fig, ax = plt.subplots(figsize=(7,6))

plt.plot(tahun, Bandung, marker='o', markerfacecolor='r', markersize=7, label="Bandung")
plt.plot(tahun, Subang, marker='*', markerfacecolor='b', markersize=7, label="Subang")

plt.xticks(tahun)

plt.xlabel("Tahun")
plt.ylabel("Jumlah Penduduk")

plt.legend()
plt.title("Grafik Persebaran Penduduk")
plt.grid()
plt.show()

"""Berdasarkan line plot yang ditampilkan, dapat disimpulkan bahwa average jumlah penduduk Kota Bandung dan Kota Subang memiliki nilai minimum 40000 dan nilai maximum 90000. Dan jumlah penduduk pada 2 kota tersebut mengalami naik-turun tiap tahunnya."""