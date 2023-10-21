import matplotlib.pyplot as plt

tahun = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
profit = [25, 37, 42, 50, 60, 64, 68, 30, 45, 50, 65, 70, 80, 82, 88]

plt.bar(tahun, profit, color='yellow')

plt.xlabel('Tahun', fontweight='bold')
plt.ylabel('Profit', fontweight='bold')
plt.title('Revenue PT Maju Mundur Tahun 2005-2019', fontweight='bold')

plt.legend(['Profit'], loc='upper left')

for i in range(len(tahun)):
    persentase = str(round((profit[i]/sum(profit))*100, 2)) + '%'
    plt.text(tahun[i]-0.4, profit[i]+1, persentase, color='black', fontweight='bold')

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.xticks(tahun, fontsize=8)
plt.yticks(profit, fontsize=8)
plt.show()

"""
Pada grafik, kita dapat melihat bahwa keuntungan naik dari tahun 2005 hingga 2009, kemudian menurun di tahun 2012 dan 2013, sebelum meningkat kembali di tahun 2014 hingga 2019. Oleh karena itu, kita dapat melihat bahwa keuntungan perusahaan tidak selalu meningkat setiap tahun dan dapat dipengaruhi oleh banyak faktor.
Selain itu, kita dapat simpulkan bahwa profit penjualan paling besar diraih pada tahun 2019 dan profit paling kecil diraih pada tahun 2005.
"""
