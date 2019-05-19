import threading
import random
import time


gMoney = 10000
glock = threading.Lock()

class Producer (threading.Thread):
    def run (self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            glock.acquire()
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            glock.release()
            time.sleep(1)

class Consumer (threading.Thread):
    def run (self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            glock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费者消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            glock.release()
            time.sleep(1)

def main():
    for x in range(3):
        t = Consumer(name="消费者线程%d" %x)
        t.start()

    for x in range(5):
        t = Producer(name="生产者线程%d" %x)
        t.start()


if __name__ == '__main__':
    main()
