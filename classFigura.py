class Figura:
    dlina = None
    shirina = None

    def setData(self,dlina,shirina):
        self.shirina = shirina
        self.dlina = dlina
    def area(self):
        return self.dlina * self.shirina
    def perimetr(self):
        return 2 * (self.dlina + self.shirina)

figura1 = Figura()
figura1.setData(5,10)
print("Площадь фигуры:",figura1.area())
print("Периметр фигуры:",figura1.perimetr())

