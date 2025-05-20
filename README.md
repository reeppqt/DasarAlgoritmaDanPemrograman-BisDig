# Dasar Algoritma dan Pemrograman - Bisnis Digital
UJIAN TENGAH SEMESTER ( Reza eka putra , 24110310068 ) 2B BISNIS DIGITAL

penjelasan dalam soal uts


# Dasar Algoritma dan Pemrograman - Bisnis Digital

Repository ini berisi solusi untuk berbagai studi kasus pemrograman dasar dalam Python.

## Daftar Program

1. **Faktorial Rekursif** - Menghitung faktorial dengan fungsi rekursif
2. **Input Nilai Siswa** - Mencari nilai tertinggi dari 5 siswa
3. **Diskon E-commerce** - Menghitung diskon berdasarkan total belanja
4. **Kasir Toko** - Menghitung total harga 3 barang
5. **Kelulusan Siswa** - Menentukan kelulusan berdasarkan rata-rata nilai

# 1. Fungsi Rekursif untuk Menghitung Faktorial

## Deskripsi
Program ini menghitung nilai faktorial dari sebuah bilangan bulat positif menggunakan pendekatan rekursif. Faktorial (n!) adalah hasil perkalian semua bilangan bulat positif dari 1 sampai n.

## Konsep Matematis
Faktorial didefinisikan sebagai:
- n! = n × (n-1) × (n-2) × ... × 1
- 0! = 1 (kondisi basis)
- 1! = 1 (kondisi basis)

Contoh:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 3! = 3 × 2 × 1 = 6

## Cara Kerja Rekursi
Fungsi rekursif bekerja dengan:
1. **Base Case**:
   - Kondisi penghentian rekursi ketika n = 0 atau 1
   - Mengembalikan nilai 1

2. **Recursive Case**:
   - Memanggil dirinya sendiri dengan parameter n-1
   - Mengalikan n dengan hasil rekursi faktorial(n-1)

---

## 2. Sistem Input Nilai Siswa

### Konsep Dasar
Program ini mengelola data nilai siswa dalam bentuk list dan mencari nilai tertinggi.

### Fitur:
- Input nilai sebanyak 5 kali (dengan `for` loop, atau `while` untuk versi dinamis).
- Menyimpan nilai dalam list.
- Menggunakan `max()` untuk mencari nilai tertinggi.
- Menentukan posisi nilai tertinggi dengan `index()`.
- Kompleksitas waktu: `O(n)`.

---

## 3. Sistem Diskon E-commerce

### Konsep Dasar
Simulasi sistem diskon berdasarkan total belanja pengguna.

### Fitur:
- Input total belanja.
- Menggunakan `if`, `else`, dan `elif` untuk menentukan tingkat diskon.
- Diskon 10% jika belanja > 500.000 (bisa dikembangkan menjadi bertingkat).
- Output diformat rapi dengan dua desimal dan tanda ribuan (`{:.2f}`).

---

## 4. Sistem Kasir Toko Sederhana

### Konsep Dasar
Menghitung total harga dari beberapa barang yang dibeli.

### Fitur:
- Loop input harga 3 kali.
- Setiap harga dikonversi ke `float`.
- Akumulasi total harga.
- Alternatif: list harga, input nama barang, validasi nilai.
- Peningkatan: hitung pajak/diskon.

---

## 5. Sistem Kelulusan Siswa

### Konsep Dasar
Menentukan status kelulusan berdasarkan rata-rata tiga nilai.

### Fitur:
- Input tiga nilai (tipe `float`).
- Hitung rata-rata.
- Bandingkan dengan batas kelulusan (75).
- Output status kelulusan (`LULUS` atau `TIDAK LULUS`).
- Peningkatan: pembobotan nilai, lulus dengan pujian (>90), histori nilai.


