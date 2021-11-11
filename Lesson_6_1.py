import time
import itertools

class TrafficLight:
    __color = [['red', 7], ['yellow', 2], ['green', 15], ['yellow', 2]]

    def running(self):
        for item in itertools.cycle(self.__color):
            print(f"{item[0]}")
            time.sleep(item[1])
trf = TrafficLight()
trf.running()
