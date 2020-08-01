#!/usr/bin/env python3
""" Two hungry people, anxiously waiting for their turn to take soup """

import threading

slowcooker_lid = threading.Lock()
soup_servings = 11
soup_taken = threading.Condition(lock=slowcooker_lid)  # Conditional Variable
NUM_OF_HUNGRY_PEOPLES = 5

def hungry_person(person_id):
    global soup_servings
    while soup_servings > 0:
        with slowcooker_lid:
            while (person_id != (soup_servings % NUM_OF_HUNGRY_PEOPLES)) and (soup_servings > 0): # check if it's your turn
                print('Person', person_id, 'checked... then put the lid back:.')
                soup_taken.wait()

            if (soup_servings > 0):
                soup_servings-=1   # it's your turn, take some soup
                print('Person', person_id, 'took soup! Serving Left:', soup_servings )

                soup_taken.notify_all() 
             

if __name__ == '__main__':
    for i in range(NUM_OF_HUNGRY_PEOPLES):
        threading.Thread(target=hungry_person, args=(i,)).start()




