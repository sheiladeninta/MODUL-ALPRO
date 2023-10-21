import numpy as np

nilaiMath = {
    "SI4601" : 78.6,
    "SI4602" : 69.4,
    "SI4603" : 86.4,
    "SI4604" : 79.7,
    "SI4605" : 89.1,
    "SI4606" : 67.9,
    "SI4607" : 78.8,
    "SI4608" : 88.6
}

nilai = list(nilaiMath.values())
nilai2 = list(nilaiMath.keys())
nilaiTertinggi = nilai2[nilai.index(np.max(nilai))]
nilaiTerendah = nilai2[nilai.index(np.min(nilai))]

print(f"Rata-rata nilai matematika dari kelas SI adalah {np.mean(nilai)}")
print(f"Nilai terendah matematika dari kelas SI adalah {np.min(nilai)} berada di {nilaiTerendah}")
print(f"Nilai tertinggi matematika dari kelas SI adalah {np.max(nilai)} berada di {nilaiTertinggi}")
print(f"Kelas {nilaiTerendah} perlu diadakan evaluasi!")