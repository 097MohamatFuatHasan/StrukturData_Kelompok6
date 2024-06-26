class Peta:
    def __init__(self):
        self.cityList = {}  # Dictionary untuk menyimpan kota-kota dan jalan antar kota
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":", self.cityList[kota])  # Mencetak kota dan daftar jalannya
        
    def tambahkanKota(self, kota):
        if kota not in self.cityList:
            self.cityList[kota] = []  # Menambahkan kota baru ke dalam dictionary sebagai key dengan daftar jalan kosong
            return True
        return False  # Mengembalikan False jika kota sudah ada
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.cityList:  # Memeriksa apakah kota yang akan dihapus ada di dictionary
            for kotalain in self.cityList:  # Mengiterasi setiap kota lain di dictionary
                if kotaDihapus in self.cityList[kotalain]:  # Jika kota yang akan dihapus ada dalam daftar jalan kota lain
                    self.cityList[kotalain].remove(kotaDihapus)  # Hapus jalan dari kota lain ke kota yang akan dihapus
            del self.cityList[kotaDihapus]  # Hapus kota dari dictionary
            return True
        return False  # Mengembalikan False jika kota tidak ditemukan

   
    def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.cityList[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #hapus kota 1 di list kota2
            self.cityList[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False
        

petaJatim = Peta()
petaJatim.tambahkanKota("Surabaya")
petaJatim.tambahkanKota("Lamongan")
petaJatim.tambahkanKota("Nganjuk")
petaJatim.tambahkanKota("Kediri")
petaJatim.tambahkanKota("Tulungagung")
petaJatim.tambahkanKota("Blitar")
petaJatim.tambahkanKota("Malang")
petaJatim.tambahkanKota("Jember")
petaJatim.tambahkanKota("Banyuwangi")
petaJatim.tambahkanKota("Probolinggo")
petaJatim.tambahkanJalan("Surabaya","Lamongan")
petaJatim.tambahkanJalan("Surabaya","Probolinggo")
petaJatim.tambahkanJalan("Surabaya","Malang")
petaJatim.tambahkanJalan("Surabaya","Nganjuk")
petaJatim.tambahkanJalan("Nganjuk","Lamongan")
petaJatim.tambahkanJalan("Kediri","Nganjuk")
petaJatim.tambahkanJalan("Kediri","Malang")
petaJatim.tambahkanJalan("Kediri","Tulungagung")
petaJatim.tambahkanJalan("Kediri","Blitar")
petaJatim.tambahkanJalan("Tulungagung","Blitar")
petaJatim.tambahkanJalan("Malang","Blitar")
petaJatim.tambahkanJalan("Malang","Probolinggo")
petaJatim.tambahkanJalan("Malang","Jember")
petaJatim.tambahkanJalan("Banyuwangi","Probolinggo")
petaJatim.tambahkanJalan("Banyuwangi","Jember")
petaJatim.tambahkanJalan("Probolinggo","Jember")
petaJatim.printPeta()
