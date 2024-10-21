# Fungsi untuk menentukan bilangan terbesar
def bilangan_terbesar(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Input dari pengguna
angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))
angka3 = float(input("Masukkan bilangan ketiga: "))

# Memanggil fungsi dan mencetak hasil
hasil = bilangan_terbesar(angka1, angka2, angka3)
print(f"Bilangan terbesar adalah: {hasil}")
