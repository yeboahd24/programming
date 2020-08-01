#!/usr/bin/env python3
""" Chopping vegetables with a ThreadPool """

import threading
from concurrent.futures import ProcessPoolExecutor
import os

def vegetable_chopper(vegetable_id):
    name = os.getpid()
    print(name, 'chopped a vegetable', vegetable_id)

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=5) as pool:
        for vegetable in range(100):
            pool.submit(vegetable_chopper, vegetable)
