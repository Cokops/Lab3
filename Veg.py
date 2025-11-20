class VegetableList(list):
    def add_veg(self, name, weight):
        self.append((name, weight))  
    def check_veg(self,name):
        for veg_name in self:
            if veg_name[0] == name:
                print(f"Да,овощ:{name} есть в списке.")
                return
        print(f"Овоща {name} нет в списке!")    
               
veg = VegetableList()

veg.add_veg("Картошка", 100)
veg.add_veg("Морковка", 50)
veg.add_veg("Лук", 30)
veg.add_veg("Я", 85)

print(veg)

veg.check_veg("Картошка")