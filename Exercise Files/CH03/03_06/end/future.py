#!/usr/bin/env python3
""" Check how many vegetables are in the pantry """

from concurrent.futures import ThreadPoolExecutor
import time

def how_many_vegetables():
    print('Olivia is counting vegetables...')
    time.sleep(3)
    return 42

if __name__ == '__main__':
    print('Barron asks Olivia how many vegetables are in the pantry.')
    with ThreadPoolExecutor() as pool:
        future = pool.submit(how_many_vegetables)
        print('Barron can do others things while he waits for the result...')
        print('Olivia responded with', future.result())
