from abc import ABC, abstractmethod

class CARS(ABC):
    @abstractmethod
    def cn(self, companyname):
        pass

    @abstractmethod
    def specie(self):
        pass


class Swift(CARS):
    def cn(self, companyname):
        print(f"Swift is the car of {companyname}")

    def specie(self):
        pass   


class Model_S(CARS):
    def cn(self, companyname):
        print(f"Model S is the car of {companyname}")

    def specie(self):
        pass


class Fortuner(CARS):
    def cn(self, companyname):
        print(f"Fortuner is the car of {companyname}")

    def specie(self):
        pass


class City(CARS):
    def cn(self, companyname):
        print(f"City is the car of {companyname}")

    def specie(self):
        pass


class Creta(CARS):
    def cn(self, companyname):
        print(f"Creta is the car of {companyname}")

    def specie(self):
        pass


n1 = Swift()
n1.cn("Maruti Suzuki")

cn2 = Model_S()
cn2.cn("Tesla")

cn3 = Fortuner()
cn3.cn("Toyota")

cn4 = City()
cn4.cn("Honda")

cn5 = Creta()
cn5.cn("Hyundai")