"""
Adi:Atakan
Soyadi:Canbakış
Numarasi:20217170006
Bolumu:Bilgisayar Mühendisliği 2.sinif

"""

class Otobus:
    """Otobus bilet satis takip sinifi"""
    plaka:str=""
    nereden:str=""
    nereye:str=""
    koltukno:int=0
    dolukoltuk:int=0
    boskoltuk:int=0
    koltuksay:int=0
    

    def __init__(self,plaka,nereden,nereye,koltuksay):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        self.plaka=plaka
        self.nereden=nereden
        self.nereye=nereye
        self.koltuksay=koltuksay
        
    def bilet_sat(self,):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        if self.koltukno==0:
            self.dolukoltuk=self.dolukoltuk
        else:
            self.dolukoltuk=+1
            

        
   
    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        if self.koltukno==0:
            self.boskoltuk=self.boskoltuk
        else:
            self.boskoltuk=-1
        
        

    
    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("{},{},{},{},{},".format(self.nereden,self.nereye,self.plaka,self.boskoltuk,self.dolukoltuk))
        


        


        


