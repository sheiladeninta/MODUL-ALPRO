import statistics as st
import numpy as np

def input_data():
    global n # variabel global untuk jumlah data
    global pengunjung # variabel global untuk menyimpan data pengunjung
    global pembeli # variabel global untuk menyimpan data pembeli
    print("=== STATISTIKA DATA PENGUNJUNG DAN PEMBELI ===")
    n = int(input("Masukkan jumlah data: "))

    pengunjung = []
    pembeli = []

    for i in range(n):
        p = int(input(f"Masukkan data pengunjung hari ke-{i+1}: "))
        pengunjung.append(p)
        b = int(input(f"Masukkan data pembeli hari ke-{i+1}: "))
        pembeli.append(b)
    return pengunjung, pembeli

def cetak_data():
    global n 
    global pengunjung
    global pembeli
    print("\n===============================\t")
    print("No.\tPengunjung\tPembeli")
    for i in range(n):
        print(f"{i+1}\t{pengunjung[i]}\t\t{pembeli[i]}")
    print("===============================\t")

def mean(data):
    rata = st.mean(data)
    return rata

def median(data):
    tengah = st.median(data)
    return tengah

def modus(data):
    try:
        sering = st.mode(data)
        return sering
    except:
        return None

def minimum(data):
    min = min(data)
    return min

def maximum(data):
    max = max(data)
    return max

def stdev(data):
    simpangan = st.stdev(data)
    return simpangan

def quartil(data):
    q1 = np.quantile(data, 0.25) # quartil pertama adalah nilai yang membagi 25% data terendah
    q2 = np.quantile(data, 0.5) # quartil kedua adalah nilai yang membagi 50% data terendah dan 50% data tertinggi, sama dengan median
    q3 = np.quantile(data, 0.75) # quartil ketiga adalah nilai yang membagi 75% data terendah
    return q1, q2, q3

def covarian(data1, data2):
    cov = np.cov(data1, data2)[0][1] 
    return cov

def korelasi(data1, data2):
    cor = np.corrcoef(data1, data2)[0][1] 
    return cor

def variansi(data):
    var = np.var(data)
    return var

def exit():
    print("Terima kasih sudah menggunakan aplikasi ini!")
    return

def menu_statistik():
    print("""
1. Mean
2. Median
3. Modus
4. Nilai minimum
5. Nilai maximum
6. Standar deviasi
7. Quartil
8. Covarian
9. Korelasi
10. Variansi
11. Exit
""")

def hasil_statistik(pilihan):
    global n 
    global pengunjung 
    global pembeli
    while True:
        pilihan = int(input("Masukkan pilihan Anda (1-10): "))
        if pilihan == 1:
            mean_pengunjung = mean(pengunjung) 
            mean_pembeli = mean(pembeli) 
            print(f"Mean data pengunjung: {mean_pengunjung}")
            print(f"Mean data pembeli: {mean_pembeli}")

        elif pilihan == 2:
            median_pengunjung = median(pengunjung)
            median_pembeli = median(pembeli) 
            print(f"Median data pengunjung: {median_pengunjung}")
            print(f"Median data pembeli: {median_pembeli}")
        
        elif pilihan == 3:
            modus_pengunjung = modus(pengunjung) 
            modus_pembeli = modus(pembeli) 
            
            if modus_pengunjung != None:
                print(f"Modus data pengunjung: {modus_pengunjung}")
            else:
                print("Tidak ada modus untuk data pengunjung")
            
            if modus_pembeli != None:
                print(f"Modus data pembeli: {modus_pembeli}")
            else:
                print("Tidak ada modus untuk data pembeli")
        
        elif pilihan == 4:
            min_pengunjung = minimum(pengunjung) 
            min_pembeli = minimum(pembeli)
            print(f"Nilai minimum data pengunjung: {min_pengunjung}")
            print(f"Nilai minimum data pembeli: {min_pembeli}")

        elif pilihan == 5:
            max_pengunjung = maximum(pengunjung) 
            max_pembeli = maximum(pembeli) 
            print(f"Nilai maximum data pengunjung: {max_pengunjung}")
            print(f"Nilai maximum data pembeli: {max_pembeli}")

        elif pilihan == 6:
            stdev_pengunjung = stdev(pengunjung) 
            stdev_pembeli = stdev(pembeli) 
            print(f"Standar deviasi data pengunjung: {stdev_pengunjung}")
            print(f"Standar deviasi data pembeli: {stdev_pembeli}")

        elif pilihan == 7:
            q1_pengunjung, q2_pengunjung, q3_pengunjung = quartil(pengunjung) 
            q1_pembeli, q2_pembeli, q3_pembeli = quartil(pembeli) 
            print(f"Quartil pertama data pengunjung: {q1_pengunjung}")
            print(f"Quartil kedua data pengunjung: {q2_pengunjung}")
            print(f"Quartil ketiga data pengunjung: {q3_pengunjung}")
            print(f"Quartil pertama data pembeli: {q1_pembeli}")
            print(f"Quartil kedua data pembeli: {q2_pembeli}")
            print(f"Quartil ketiga data pembeli: {q3_pembeli}")
        
        elif pilihan == 8:
            cov = covarian(pengunjung, pembeli) 
            print(f"Covarian data pengunjung dan pembeli: {cov}")
        
        elif pilihan == 9:
            cor = korelasi(pengunjung, pembeli)
            print(f"Korelasi data pengunjung dan pembeli: {cor}")
        
        elif pilihan == 10:
            var_pengunjung = variansi(pengunjung) 
            var_pembeli = variansi(pembeli) 
            print(f"Variansi data pengunjung: {var_pengunjung}")
            print(f"Variansi data pembeli: {var_pembeli}")

        elif pilihan == 11:
            exit()
            break
        
        else:
            print("Pilihan tidak valid. Silakan masukkan angka dari 1 sampai 10.")

if __name__ == "__main__":
    pengunjung, pembeli = input_data()
    cetak_data()
    pilihan = menu_statistik()
    hasil_statistik(pilihan)