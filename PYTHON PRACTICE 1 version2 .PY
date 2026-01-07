from abc import ABC, abstractmethod

class CARS(ABC):
    @abstractmethod
    def cn(self, companyname):
        pass

    @abstractmethod
    def specie(self,speciality):
        self.speciality = speciality
        pass

class Swift(CARS):
    def cn(self, companyname):
        print(f"Swift is the car of {companyname}")

    def specie(self,speciality):
        self.speciality = speciality
        print(f"Specie: {self.speciality}")

class Model_S(CARS):
    def cn(self, companyname):
        print(f"Model S is the car of {companyname}")

    def specie(self,speciality):
        self.speciality = speciality
        print(f"Specie: {self.speciality}")

class Fortuner(CARS):
    def cn(self, companyname):
        print(f"Fortuner is the car of {companyname}")

    def specie(self,speciality):
        self.speciality = speciality
        print(f"Specie: {self.speciality}")

class City(CARS):
    def cn(self, companyname):
        print(f"City is the car of {companyname}")

    def specie(self,speciality):
        self.speciality = speciality
        print(f"Specie: {self.speciality}")

class Creta(CARS):
    def cn(self, companyname):
        print(f"Creta is the car of {companyname}")

    def specie(self,speciality):
        self.speciality = speciality
        print(f"Specie: {self.speciality}")

# Objects
n1 = Swift()
n1.cn("Maruti Suzuki")
n1.specie("Hatchback")

cn2 = Model_S()
cn2.cn("Tesla")
cn2.specie("Electric Sedan")

cn3 = Fortuner()
cn3.cn("Toyota")
cn3.specie("SUV")

cn4 = City()
cn4.cn("Honda")
cn4.specie( "Sedan")

cn5 = Creta()
cn5.cn("Hyundai")
cn5.specie("Compact SUV")


