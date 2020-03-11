class Manusia(object):
    """ Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'

    def __init__(self, nama):
        self.nama = nama

    def ucapkanSalam(self):
        print('Salam, namaku', self.nama)

    def makan(self, s):
        print('saya baru saja makan', s)
        self.keadaan = 'kenyang'

    def olahraga(self, k):
        print('saya baru saja latihan', k)
        self.keadaan = 'lapar'

    def mengaliDenganDua(self, n):
        return n * 2


class Mahasiswa(Manusia):
    """Class Mahasiswa yg dibangun dari class Manusia"""
    def __init__(self, nama, NIM, kota, us):
        """ Metode ini menutupi inisiasi dari class Manusia """
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
        """ Method ini menutupi method di Manusia """
        print('Saya baru saja makan', s, 'sambil belajar')
        self.keadaan = 'kenyang'


    # 4
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
    # 5
    def hapusKuliah(self, item):
        self.listKuliah.remove(item)
