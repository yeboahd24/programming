GeneralFare = 60
Percentage = 100
Student = 20
Couples = 15
AboveAge = 35
LIMIT = 3

def travel():
	user = int(input('Student or OlderPerson or Couples [1-3] respectively: '))
	while user > LIMIT:
		print('Out of range....')
		break
	if user == 1:
		age = int(input('age: '))
		if age < 20:
			totalFare = (Student/Percentage)*GeneralFare
			print(f'Your total discount is {totalFare}')
		print('No discount at this point.')
		
	elif user == 2:
		age = int(input('age: '))
		if age > 60:
			totalFare = (AboveAge/Percentage)*GeneralFare
			print(f'Your discount is: {totalFare}')
		print('No discount at this point.')

	else:
		totalFare = (Couples/Percentage)*GeneralFare
		print(f'Your discount is: {totalFare}')
	

travel()

