# -*- coding: utf-8 -*-
"""nilai rata rata

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17nCX4_S2pjp-faert3bcW92wz0-YXYUo
"""

nilai1 = float(input("Masukkan nilai pelajaran 1: "))
nilai2 = float(input("Masukkan nilai pelajaran 2: "))
nilai3 = float(input("Masukkan nilai pelajaran 3: "))

rata_rata = (nilai1 + nilai2 + nilai3) / 3

if rata_rata >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print(f"Rata-rata nilai: {rata_rata:.2f}")
print(f"Status: {status}")