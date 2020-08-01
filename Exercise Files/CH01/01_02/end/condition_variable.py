#!/usr/bin/env python3
""" Two hungry people, anxiously waiting for their turn to take soup """

import threading

slowcooker_lid = threading.Lock()
soup_servings = 11
soup_taken = threading.Condition(lock=slowcooker_lid)

def hungry_person(person_id):
    global soup_servings
    while soup_servings > 0:
        with slowcooker_lid:
            while (person_id != (soup_servings % 5)) and (soup_servings > 0): # check if it's your turn
                print('Person', person_id, 'checked... then put the lid back.')
                soup_taken.wait()
            if (soup_servings > 0):
                soup_servings -= 1 # it's your turn; take some soup!
                print('Person', person_id, 'took soup! Servings left:', soup_servings)
                soup_taken.notify_all()

if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=hungry_person, args=(i,)).start()
