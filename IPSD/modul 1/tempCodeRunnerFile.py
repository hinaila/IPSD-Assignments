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
