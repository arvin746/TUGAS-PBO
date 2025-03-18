class Karyawan:
    def __init__(self, nama, jabatan, gaji, tanda_pengenal):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
        self.tanda_pengenal = tanda_pengenal

    def mengejar_target(self, target):
        print(f"{self.nama} dengan jabatan {self.jabatan} sedang mengejar target {target}.")

    def kontrak_kerja(self, durasi):
        print(f"{self.nama} memiliki kontrak kerja selama {durasi} bulan.")

    def pelatihan(self, bidang):
        print(f"{self.nama} mengikuti pelatihan di bidang {bidang}.")

karyawan1 = Karyawan("Rini", "Manajer Penjualan", 12000000, "ID12345")

print(f"Nama: {karyawan1.nama}")
print(f"Jabatan: {karyawan1.jabatan}")
print(f"Gaji: Rp{karyawan1.gaji}")
print(f"Tanda Pengenal: {karyawan1.tanda_pengenal}")

karyawan1.mengejar_target("Peningkatan Penjualan 20%")
karyawan1.kontrak_kerja(12)
karyawan1.pelatihan("Leadership")