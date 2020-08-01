#!/usr/bin/env python3
""" Producers serving soup for Consumers to eat """

import queue
import threading
import time
import multiprocessing as mp

serving_line = mp.Queue(5)

def cpu_work(work_units):
    x = 0
    for i in range(work_units*1_000_000):
        x += 1

def soup_producer(serving_line):
    for i in range(20): # serve 20 bowls of soup
        serving_line.put_nowait('Bowl #'+str(i))
        print('Served Bowl #', str(i), '- remaining capacity:', \
            serving_line._maxsize-serving_line.qsize())
        time.sleep(0.2) # time to serve a bowl of soup
    serving_line.put_nowait('no soup for you!')
    serving_line.put_nowait('no soup for you!')

def soup_consumer(serving_line):
    while True:
        bowl = serving_line.get()
        if bowl == 'no soup for you!':
            break
        print('Ate', bowl)
        cpu_work(5) # time to eat a bowl of soup

if __name__ == '__main__':
    for i in range(2):
        mp.Process(target=soup_consumer, args=(serving_line,)).start()
    mp.Process(target=soup_producer, args=(serving_line,)).start()
