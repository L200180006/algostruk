class MhsTIF(object):
   
    def __init__(self,nama,NIM,asal,saku):
        self.nama = nama
        self.NIM = NIM
        self.asal = asal
        self.saku = saku
        
c0 = MhsTIF ('Ika','L200180001','Sukoharjo', 240000)
c1 = MhsTIF ('Budi','L200180010','Sragen', 230000)
c2 = MhsTIF ('Ahmad','L200180002','Surakarta', 250000)
c3 = MhsTIF ('Chandra','L200180004','Surakarta', 230000)
c4 = MhsTIF ('Eka','L200180005','Boyolali', 240000)
c5 = MhsTIF ('Fandi','L20018006','Salatiga', 250000)
c6 = MhsTIF ('Deni','L200180007','Klaten', 245000)
c7 = MhsTIF ('Galuh','L20018008','Wonogiri', 245000)
c8 = MhsTIF ('Janto','L200180009','Klaten', 245000)
c9 = MhsTIF ('Hasan','L2001800011','Karanganyar', 270000)
c10 = MhsTIF ('Khalid','L200180012','Purwodadi', 265000)
Mhs = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def urutkan(A):
    baru = {}
    for i in range(len(A)):
        baru[A[i].nama] = A[i].NIM
    listofTuples = sorted(baru.items(), key = lambda x: x[1])
    for elemen in listofTuples :
        print(elemen[0], ":", elemen[1])


