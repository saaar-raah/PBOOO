#from Pasien import Pasien
#from Dokter import Dokter

class RekamKesehatanElektronik:

    def __init__(self, Dokter, Daftar_RKE, Diagnosa):
        self.__Dokter= []
        self.__Daftar_RKE= []
        self.__Diagnosa = []

@property
    def Diagnosa(self):
        return self.__Diagnosa    
    @Diagnosa.setter
    def Diagnosa(self, Diagnosa=[]):
        self.__Diagnosa = []

@property
    def Daftar_RKE(self):
        return self.__Daftar_RKE    
    @Daftar_RKE.setter
    def Daftar_RKE(self, Daftar_RKE=[]):
        self.__Daftar_RKE = []

  @property
    def Diagnosa(self):
        return self.__Diagnosa    
    @Diagnosa.setter
    def Diagnosa(self, Diagnosa=[]):
        self.__Diagnosa = []

    def __str__(self):
        return "Dokter : {} \n  Daftar_RKE : {}\n Diagnosa : {}".format(self.Dokter,self.Daftar_RKE,self.Diagnosa)