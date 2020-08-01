#!/usr/bin/env python3
""" Deciding how many bags of chips to buy for the party """

import threading

bags_of_chips = 1 # start with one on the list
pencil = threading.Lock()

def cpu_work(work_units):
    x = 0
    for i in range(work_units*1_000_000):
        x += 1

def barron_shopper():
    global bags_of_chips
    cpu_work(1) # do a bit of work first
    with pencil:
        bags_of_chips *= 2
        print('Barron DOUBLED the bags of chips.')

def olivia_shopper():
    global bags_of_chips
    cpu_work(1) # do a bit of work first
    with pencil:
        bags_of_chips += 3
        print('Olivia ADDED 3 bags of chips.')

if __name__ == '__main__':
    shoppers = []
    for i in range(5):
        shoppers.append(threading.Thread(target=barron_shopper))
        shoppers.append(threading.Thread(target=olivia_shopper))
    for s in shoppers:
        s.start()
    for s in shoppers:
        s.join()
    print('We need to buy', bags_of_chips, 'bags of chips.')
