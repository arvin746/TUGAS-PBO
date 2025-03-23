class Karyawan:
    def __init__(self, nama, jabatan, gaji, tanda_pengenal):
        self.nama = nama
        self.jabatan = jabatan
        self.__gaji = gaji
        self.__tanda_pengenal = tanda_pengenal

    def mengejar_target(self, target):
        print(f"{self.nama} dengan jabatan {self.jabatan} sedang mengejar target {target}.")

    def kontrak_kerja(self, durasi):
        print(f"{self.nama} memiliki kontrak kerja selama {durasi} bulan.")

    def pelatihan(self, bidang):
        print(f"{self.nama} mengikuti pelatihan di bidang {bidang}.")

    def get_gaji(self):
        return self.__gaji

    def set_gaji(self, gaji_baru):
        self.__gaji = gaji_baru

    def get_tanda_pengenal(self):
        return self.__tanda_pengenal

    def set_tanda_pengenal(self, tanda_pengenal_baru):
        self.__tanda_pengenal = tanda_pengenal_baru

karyawan2 = Karyawan("Budi", "Supervisor", 8000000, "ID67890")

print(f"Nama: {karyawan2.nama}")
print(f"Jabatan: {karyawan2.jabatan}")
print(f"Gaji (sebelum diubah): Rp{karyawan2.get_gaji()}")
karyawan2.set_gaji(9000000)
print(f"Gaji (setelah diubah): Rp{karyawan2.get_gaji()}")

print(f"Tanda Pengenal (sebelum diubah): {karyawan2.get_tanda_pengenal()}")
karyawan2.set_tanda_pengenal("ID99999")
print(f"Tanda Pengenal (setelah diubah): {karyawan2.get_tanda_pengenal()}")

karyawan2.mengejar_target("Optimasi Operasional")
karyawan2.kontrak_kerja(24)
karyawan2.pelatihan("Manajemen Risiko")
