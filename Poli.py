# from Dokter import Dokter


class Poli:
    def __init__(self):
        self.__jenis_poli = []
        self.__daftar_dokter = []

    def getJenis_poli(self):
        return "Jenis Poli : ", format(self.__jenis_poli)

    def setJenis_poli(self, jenis):
        self.__jenis_poli.append(jenis)

    def getDaftar_dokter(self):
        return "Daftar Dokter : ", format(self.__daftar_dokter)

    def setDaftar_dokter(self, daftar):
        self.__daftar_dokter.append(daftar)


a = Poli()
# d = Dokter()
a.setDaftar_dokter(input("Masukkan Dokter :"))
a.setJenis_poli(input("Masukkan Jenis Poli :"))
print(a.getJenis_poli())
print(a.getDaftar_dokter())
# print(d.getJadwalDokter())
