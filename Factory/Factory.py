class Car:
    def get_wheels(self) -> int:
        return -1


class MiniCar(Car):
    def get_wheels(self) -> int:
        return 4


class LorryCar(Car):
    def get_wheels(self) -> int:
        return 12


class CarFactory:
    def get_car(self, brand) -> Car:
        if brand == "Mini":
            return MiniCar()
        elif brand == "Lorry":
            return LorryCar()
        return None


car1 = CarFactory().get_car("Mini")
print(car1.get_wheels())

car2 = CarFactory().get_car("Lorry")
print(car2.get_wheels())
