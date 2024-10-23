def cari_bilangan_terbesar():
    angka = []
    while True:
        n = float(input("Masukkan bilangan (atau 0 untuk menghentikan): "))
        if n == 0:
            break
        angka.append(n)
    if angka:
        terbesar = max(angka)
        print("Bilangan terbesar adalah:", terbesar)
    else:
        print("Tidak ada bilangan yang diinputkan.")

cari_bilangan_terbesar()