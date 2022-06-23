import time


class TrafficLight:
    __color = str

    def running(self):
        while True:
            __color = 'красный'
            print(__color)
            time.sleep(7)

            __color = 'жёлтый'
            print(__color)
            time.sleep(2)

            __color = 'зелёный'
            print(__color)
            time.sleep(7)


tl = TrafficLight()
tl.running()
