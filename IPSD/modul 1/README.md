# <h1 align="center">Laporan Praktikum Modul Dasa-Dasar Python untuk Sains Data</h1>
<p align="center">Hafshoh Imroatun Naila</p>
<p align="center">2311110056</p>

### Dasar Teori

## Variabel dan Tipe Data
Variabel  adalah  tempat  menyimpan  data  di  memori.  Nama  variabel  harus  deskriptif  dan mengikuti aturan penamaan, seperti menggunakan huruf, angka, atau underscore (_), dan tidak boleh diawali dengan angka. 
Tipe data di Python adalah jenis nilai yang dapat diolah.
•  Integer (int): Bilangan bulat positif atau negatif, misalnya 10, -3.
•  Float: Bilangan desimal atau pecahan, misalnya 3.14, -2.5.
•  String  (str):  Rangkaian  karakter  yang  didefinisikan  dengan  tanda  kutip,  misalnya "Data Science".
•  Boolean (bool): Menyatakan nilai benar atau salah, yaitu True atau False. 

## Operator dan Logika
Operator digunakan untuk melakukan operasi matematika dan logika. Berikut jenis-jenis operator yang sering digunakan di Python: 
1. Operator Aritmatika : Operator  yang  digunakan  untuk  operasi  matematis  seperti  penjumlahan,  pengurangan, perkalian, pembagian, dan eksponensial.
2. Operator Perbandingan : Operator  perbandingan  digunakan  untuk  membandingkan  dua  nilai,  hasilnya  adalah boolean (True atau False). 
3. Operator Logika : Operator logika digunakan untuk menggabungkan ekspresi boolean. 


## Unguided 
```
# Fungsi untuk memeriksa apakah suatu angka adalah bilangan prima
def bilangan_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fungsi untuk menghasilkan bilangan prima hingga jumlah yang dibutuhkan
def hasil_bilangan_prima(count):
    primes = []
    num = 2
    while len(primes) < count:
        if bilangan_prima(num):
            primes.append(num)
        num += 1
    return primes

# Fungsi untuk mencetak pola berdasarkan bilangan prima
def cetak_pola(rows):
    total_primes_needed = sum(range(1, rows + 1))  # Hitung total bilangan prima yang dibutuhkan
    primes = hasil_bilangan_prima(total_primes_needed)  # Hasilkan bilangan prima sebanyak yang dibutuhkan

    index = 0
    for i in range(1, rows + 1):
        for j in range(i):
            print(primes[index], end=" ")
            index += 1
        print()

# Jumlah baris pola yang ingin dicetak
rows = 4
cetak_pola(rows)
```
#### Output:
![Screenshot (1251)](https://github.com/user-attachments/assets/977ea653-2e84-404c-a308-d4896b2ec1dd)

```
def menggabungkan_indeks(list1, list2):
    """Mengambil elemen dengan indeks ganjil dari dua list dan mengembalikannya secara descending."""
    # Mengambil elemen dengan indeks ganjil
    elemen_indeks_ganjil = []
    
    for i in range(len(list1)):
        if i % 2 != 0:  # Memeriksa indeks ganjil
            elemen_indeks_ganjil.append(list1[i])
    
    for i in range(len(list2)):
        if i % 2 != 0:  # Memeriksa indeks ganjil
            elemen_indeks_ganjil.append(list2[i])
    
    # Mengurutkan list baru secara menurun
    elemen_indeks_ganjil.sort(reverse=True)
    
    return elemen_indeks_ganjil

# Contoh penggunaan
list1 = [1, 3, 8, 12, 15]
list2 = [10, 20, 30, 40, 50]
result = menggabungkan_indeks(list1, list2)
print(result)
```

![Screenshot (1252)](https://github.com/user-attachments/assets/9a0b1f27-87fd-459b-b1f8-37f361e525d0)


```
pin = "2510"  
saldo = 1000000      
maks_percobaan = 3      
percobaan = 0         

# masukkan PIN
while percobaan < maks_percobaan:
    pin = input("Masukkan PIN: ")
    if pin == pin:
        print("PIN benar! silakan lanjutkan.")
        break
    else:
        percobaan += 1
        print(f"PIN salah! anda memiliki {maks_percobaan - percobaan} percobaan tersisa.")
        
if percobaan == maks_percobaan:
    print("habis batas percobaan PIN. Akun terkunci.")
else:
    # uang yang ingin ditarik
    try:
        jumlah_tarik = float(input("Masukkan jumlah yang ingin ditarik: "))
        # memeriksa saldo
        if jumlah_tarik > saldo:
            print("Saldo tidak mencukupi untuk penarikan.")
        else:
            saldo -= jumlah_tarik
            print(f"penarikan berhasil! saldo akhir adalah: {saldo:.2f}")
    except ValueError:
        print("masukkan jumlah yang valid.")
```

![Screenshot (1253)](https://github.com/user-attachments/assets/48eaf42a-badb-4a7b-960b-a4a1a33bddc6)


```
!pip install pandas

import pandas as pd
import csv


#  membaca file CSV dan simpan di dict
def csvdict (namafile):
    data = {}
    with open (namafile, mode='r') as file:
        bacacsv = csv.reader(file)
        next(bacacsv)  # membaca header
        for baris in bacacsv:
            nama = baris[0]  
            nilai = list(map(float, baris[1:]))  # jadikan float
            data[nama] = nilai  
    return data

#  menghitung rata2 semua mhs
def hitungrata2(data):
    rata2 = {}
    for nama, nilai in data.items():
        if nilai:  # cek daftar nilai 
           rata2[nama] = sum(nilai) / len(nilai)  
    return rata2

# menemukan nilai rata2 tertinggi dan terendah
def caritertinggiterendah(rata2):
    tertinggi = max(rata2, key=rata2.get)
    terendah = min(rata2, key=rata2.get)
    return tertinggi, terendah

# main
def main():
    namafile = 'C:/Users/HP/OneDrive/Dokumen/C++/IPSD/modul 1/siswa_nilai.csv'  # Ubah sesuai dengan jalur file di sistem Anda
    data = csvdict (namafile)
    
    rata2 = hitungrata2(data)
    print("Rata-rata nilai tiap mahasiswa:")
    for nama, avg in rata2.items():
        print(f"{nama}: {avg:.2f}")
    
    tertinggi, terendah = caritertinggiterendah (rata2)
    print(f"\nMahasiswa dengan nilai rata-rata tertinggi: {tertinggi} ({rata2[tertinggi]:.2f})")
    print(f"Mahasiswa dengan nilai rata-rata terendah: {terendah} ({rata2[terendah]:.2f})")

if _name_ == "_main_":
    main()
```

```
import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)  # Komputer memilih angka acak
    jumlah_percobaan = 5

    print("Selamat datang permainan Tebak Angka!")
    print("Saya telah memilih angka antara 1 sampai 100.")
    print(f"Anda memiliki {jumlah_percobaan} percobaan untuk menebak angka tersebut.")

    for percobaan in range(1, jumlah_percobaan + 1):
        try:
            tebakan = int(input(f"Percobaan {percobaan}: Masukkan tebakan Anda: "))
        except ValueError:
            print("Harap masukkan angka yang valid.")
            continue

        if tebakan < 1 or tebakan > 100:
            print("Tebakan harus berada di antara 1 dan 100. Coba lagi.")
            continue

        if tebakan < angka_rahasia:
            print("Tebakan Anda terlalu kecil.")
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu besar.")
        else:
            print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dengan benar:)")
            break

    else:
        print(f"Anda telah habis percobaan. Angka yang benar adalah {angka_rahasia}:(). Coba lagi lain kali!")

# Menjalankan permainan
tebak_angka()
```

![Screenshot (1254)](https://github.com/user-attachments/assets/dfe42990-b160-472e-bcab-34d06094f865)


```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def urutan_factorial(n):
    """Fungsi untuk menghasilkan urutan faktorial dari 1 hingga n."""
    urutan = []
    for i in range(1, n + 1):
        urutan.append(factorial(i))
    return urutan

# Input dari pengguna
n = 4
hasil = urutan_factorial(n)

# Menampilkan hasil
print(", ".join(map(str, hasil)))
```
![Screenshot (1255)](https://github.com/user-attachments/assets/8f080e8e-a09b-4715-b26d-f3adff515b04)

```
def minimum_coins(amount, coins):
    """Menghitung jumlah minimum koin yang diperlukan untuk mencapai 'amount'."""
    # Menginisialisasi tabel untuk menyimpan solusi minimum koin
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Tidak ada koin diperlukan untuk jumlah 0
    coin_used = [0] * (amount + 1)  # Menyimpan koin yang digunakan

    # Iterasi melalui setiap koin
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:  # Jika kombinasi baru lebih baik
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin  # Simpan koin yang digunakan

    # Jika tidak ada solusi
    if dp[amount] == float('inf'):
        return -1, []

    # Mengembalikan jumlah koin dan kombinasi koin yang digunakan
    used_coins = []
    while amount > 0:
        used_coins.append(coin_used[amount])
        amount -= coin_used[amount]

    return dp[amount], used_coins

# Input dari pengguna
try:
    amount = int(input("Masukkan jumlah uang: "))
    coins = list(map(int, input("Masukkan nilai koin (pisah dengan spasi): ").split()))
    
    # Menentukan jumlah minimum koin
    result, used_coins = minimum_coins(amount, coins)

    if result == -1:
        print("Tidak mungkin untuk mencapai jumlah tersebut dengan koin yang diberikan.")
    else:
        print(f"Jumlah minimum koin yang diperlukan: {result}")
        print(f"Kombinasi koin yang digunakan: {used_coins}")
except ValueError:
    print("Harap masukkan angka yang valid.")
```

![Screenshot (1257)](https://github.com/user-attachments/assets/b0a0a633-fc17-40ee-866c-84c65224b4bd)


```
def reverse_words(input_string):
    """Mengonversi string menjadi list kata-kata terbalik."""
    # Memecah string menjadi list kata
    words = input_string.split()
    
    # Mengonversi setiap kata menjadi terbalik
    reversed_words = [word[::-1] for word in words]
    
    return reversed_words

# Input dari pengguna
user_input = input("Masukkan string: ")
result = reverse_words(user_input)

# Menampilkan hasil
print(result)
```

![Screenshot (1258)](https://github.com/user-attachments/assets/96bc8b1c-fe9b-4285-a479-b4d61f23570e)

```
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        """Inisialisasi atribut buku."""
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_informasi(self):
        """Menampilkan informasi buku."""
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}"

    def hitung_usia(self):
        """Menghitung usia buku berdasarkan tahun saat ini."""
        from datetime import datetime
        tahun_sekarang = datetime.now().year
        return tahun_sekarang - self.tahun_terbit


# Membuat objek dari class Buku
buku1 = Buku("Belajar Python", "Budi Santoso", 2020)
buku2 = Buku("Data Science untuk Pemula", "Siti Aminah", 2021)
buku3 = Buku("Algoritma dan Pemrograman", "Joko Widodo", 2018)

# Menampilkan informasi dan usia masing-masing buku
for buku in [buku1, buku2, buku3]:
    print(buku.tampilkan_informasi())
    print(f"Usia Buku: {buku.hitung_usia()} tahun\n")
```

![Screenshot (1259)](https://github.com/user-attachments/assets/e1e2e911-31a2-4196-b404-456aebff609f)

```
def binary_search(arr, target):
    """Melakukan pencarian biner untuk menemukan target dalam list."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Mengembalikan indeks jika ditemukan
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # Mengembalikan -1 jika tidak ditemukan

def main():
    # List angka genap yang sudah diurutkan
    even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    # Input dari pengguna
    try:
        target = int(input("Masukkan angka yang ingin dicari: "))
        
        if target % 2 != 0:
            print("Nilai tidak bisa ditemukan karena angka ganjil tidak diizinkan.")
        else:
            result = binary_search(even_numbers, target)
            if result != -1:
                print(f"Angka {target} ditemukan pada indeks {result}.")
            else:
                print(f"Angka {target} tidak ditemukan dalam list.")
                
    except ValueError:
        print("Harap masukkan angka yang valid.")

# Menjalankan program
main()
```

![Screenshot (1260)](https://github.com/user-attachments/assets/2d91329e-8e31-4837-8ce0-850e75e9e2dc)

