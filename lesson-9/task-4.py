class Car:
    is_police = bool

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction: str):
        print(f'{self.name} повернула на ' + direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    is_police = False

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышение скорости')
        else:
            print(self.speed)


class SportCar(Car):
    is_police = False

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)


class WorkCar(Car):
    is_police = False

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышение скорости')
        else:
            print(self.speed)


class PoliceCar(Car):
    is_police = True

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)


town_car = TownCar(speed=70, color='green', name='TownCar')
sport_car = SportCar(speed=150, color='green', name='SportCar')
work_car = WorkCar(speed=80, color='green', name='WorkCar')
police_car = PoliceCar(speed=160, color='green', name='PoliceCar')

town_car.go()
town_car.turn('лево')
town_car.show_speed()
town_car.stop()

sport_car.go()
sport_car.turn('лево')
sport_car.show_speed()
sport_car.stop()

work_car.go()
work_car.turn('лево')
work_car.show_speed()
work_car.stop()

police_car.go()
police_car.turn('лево')
police_car.show_speed()
police_car.stop()
