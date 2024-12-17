import random
import time
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan array acak
def buat_array(n, nilai_maksimum, seed=42):
    random.seed(seed)
    return [random.randint(1, nilai_maksimum) for _ in range(n)]

# Fungsi untuk mengecek apakah elemen dalam array unik
def cek_keunikan(array):
    sudah_dilihat = set()
    duplikat = set()
    for angka in array:
        if angka in sudah_dilihat:
            duplikat.add(angka)
        sudah_dilihat.add(angka)
    return len(duplikat) == 0, duplikat

# Fungsi untuk mengukur waktu eksekusi
def ukur_waktu(n, nilai_maksimum, percobaan=10):
    waktu_terburuk = 0
    total_waktu = 0

    for _ in range(percobaan):
        arr = buat_array(n, nilai_maksimum)

        # Mengukur waktu untuk pengecekan keunikan
        waktu_mulai = time.perf_counter()
        unik, duplikat = cek_keunikan(arr)
        waktu_berlalu = time.perf_counter() - waktu_mulai

        total_waktu += waktu_berlalu
        waktu_terburuk = max(waktu_terburuk, waktu_berlalu)

    rata_rata_waktu = total_waktu / percobaan
    return waktu_terburuk, rata_rata_waktu

# Parameter
stambuk_3_digit_terakhir = 46  # Ganti dengan 3 digit terakhir stambuk Anda
nilai_maksimum = 250 - int(f"{stambuk_3_digit_terakhir:03}")
ukuran_array = [100, 150, 200, 250, 300, 350, 400, 500]

# Pengumpulan data
hasil_terburuk = []
hasil_rata_rata = []

for n in ukuran_array:
    print(f"\nUkuran Array: {n}")
    arr = buat_array(n, nilai_maksimum)
    unik, duplikat = cek_keunikan(arr)

    if unik:
        print("Array ini unik.")
    else:
        print(f"Array ini tidak unik. Duplikat: {sorted(duplikat)}")

    waktu_terburuk, waktu_rata_rata = ukur_waktu(n, nilai_maksimum)
    hasil_terburuk.append(waktu_terburuk)
    hasil_rata_rata.append(waktu_rata_rata)

    print(f"Worst Case: {waktu_terburuk:.6f} detik")
    print(f"Average Case: {waktu_rata_rata:.6f} detik")

# Plot hasil
plt.figure(figsize=(10, 6))
plt.plot(ukuran_array, hasil_terburuk, label="Worst Case", marker="o")
plt.plot(ukuran_array, hasil_rata_rata, label="Average Case", marker="o")

plt.title("Kinerja Pengecekan Keunikan")
plt.xlabel("Ukuran Array (n)")
plt.ylabel("Waktu (detik)")
plt.legend()
plt.grid()
plt.show()

with open("worst_avg.txt", "w") as file:
    file.write("Ukuran Array | Waktu Terburuk (detik) | Waktu Rata-Rata (detik)\n")
    file.write("-" * 50 + "\n")
    for i, n in enumerate(ukuran_array):
        file.write(f"{n:<13} | {hasil_terburuk[i]:<21.6f} | {hasil_rata_rata[i]:.6f}\n")

print("\nData waktu kasus terburuk dan rata-rata telah disimpan ke dalam file 'worst_avg.txt'.")