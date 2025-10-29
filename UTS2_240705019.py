# Program Queue Pengunjung Kafe dengan laporan akhir

class Queue:
    def __init__(self):   # gunakan __init__ (dua garis bawah)
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def tampilkan(self):
        for item in self.items:
            print(item, end=" ")
        print()


# Program utama
antrian = Queue()
pesanan_selesai = []  # menyimpan hasil pesanan semua konsumen

jumlah = int(input("Masukkan jumlah konsumen = "))

# Input nama konsumen
for i in range(1, jumlah + 1):
    nama = input(f"Pelanggan {i} = ")
    antrian.enqueue(nama)

# Cetak semua antrian awal
print("\nCetak Pelanggan =", end=" ")
antrian.tampilkan()
print()

# Simulasi: satu per satu dilayani
while not antrian.is_empty():
    keluar = antrian.dequeue()
    print(f"Simulasi = {keluar}")
    pesanan = input("Pesan apa? : ")
    print(f"{keluar}, {pesanan}")
    pesanan_selesai.append((keluar, pesanan))  # simpan hasil pesanan
    print()

# Cetak daftar pesanan akhir
print("=== Daftar Pesanan Selesai ===")
for nama, pesanan in pesanan_selesai:
    print(f"{nama} - {pesanan}")
