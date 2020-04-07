from latihan2 import mergeSort
from latihan3 import quickSort
class Mahasiswa:
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM

    def ambilUangSaku(self):
        return self.uangSaku

    def makan(self, s):
        print('Saya baru saja makan', s, 'sambil belajar')
        self.keadaan = 'kenyang'

c0 = Mahasiswa("Ika", 10, "Sukoharjo", 240000)
c1 = Mahasiswa("Budi", 51, "Sragen", 230000)
c2 = Mahasiswa("Ahmad", 2, "Surakarta", 250000)
c3 = Mahasiswa("Chandra", 18, "Surakarta", 235000)
c4 = Mahasiswa("Eka", 4, "Boyolali", 240000)

daftar = [c0.NIM, c1.NIM, c2.NIM, c3.NIM, c4.NIM]
mergeSort(daftar)
print(daftar)
