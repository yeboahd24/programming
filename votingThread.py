#Number of peoples voting on election day.
from time import sleep
import threading


voting = threading.Semaphore(1)  # voting slot

def voting_box():
	name = threading.current_thread().getName()
	with voting:
		print(name, 'is voting...')
		sleep(2)
		print(name, 'is DONE voting...')

if __name__=='__main__':
	for names in range(1, 11):
		threading.Thread(target=voting_box, name='number-'+str(names)).start()