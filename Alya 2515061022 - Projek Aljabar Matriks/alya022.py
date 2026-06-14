class MATRIKS:
    def __init__(self, data):
        self.data  = data
        self.baris = len(data)
        self.kolom = len(data[0])
        self.shape = (self.baris, self.kolom)
        self.dtype = type(data[0][0]).__name__

    def format_matriks(self):
        hasil = ""
        for brs in self.data:
            hasil += str(brs) + "\n"
        return hasil

    def __repr__(self):
        return (
            f"Alya Array\n"
            f"{self.format_matriks()}\n"
            f"Tipe Data = {self.dtype}\n"
            f"Ukuran = {self.shape}"
        )

    def penjumlahan(self, lain):
        hasil = [[self.data[i][j] + lain.data[i][j] for j in range(self.kolom)] for i in range(self.baris)]
        return MATRIKS(hasil)

    def pengurangan(self, lain):
        hasil = [[self.data[i][j] - lain.data[i][j] for j in range(self.kolom)] for i in range(self.baris)]
        return MATRIKS(hasil)

    def perkalian(self, lain):
        hasil = [[sum(self.data[i][k] * lain.data[k][j] for k in range(self.kolom)) for j in range(lain.kolom)] for i in range(self.baris)]
        return MATRIKS(hasil)
