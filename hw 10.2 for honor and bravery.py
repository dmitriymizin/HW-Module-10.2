from threading import Thread, Lock
import time

class Knight(Thread):
    warriors = 100
    lock = Lock()

    def __init__(self, name_knight, power_knight):
        self.name_knight = name_knight
        self.power_knight = power_knight
        super().__init__()

    def run(self):
        with Knight.lock:
            print(f'{self.name_knight}, на нас напали!')
        ii = 0
        for i in range(1, self.warriors, self.power_knight):
            self.warriors -= self.power_knight
            time.sleep(1)
            ii += 1
            with Knight.lock:
                print(f'{self.name_knight} сражается {ii} дней, осталось {self.warriors} воинов')
        with Knight.lock:
            print(f'{self.name_knight} одержал победу спустя {ii} дней')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread1 = first_knight
thread2 = second_knight

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Все битвы закончились')






