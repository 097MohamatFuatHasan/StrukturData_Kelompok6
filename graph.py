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
