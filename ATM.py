
'''This is a simple ATM machine code.'''
while True:
	balance = 100_000
	prompt = '''
	Welcome To Linux ATM Machine,
	Please Follow All the Instructions
	To Make Everything Easy For You
	Thank You.'''

	print(prompt)
	print(' ')
	print('	 ATM  ')
	print(' ')
	print('''
		1)		Balance
		2)		Withdraw
		3)		Deposit
		4)		Quit
		''')
	try:
		Option = int(input("Enter Option: "))
	except Exception as e:
		print("Error:", e)
		print("Enter 1,2,3 or 4 only")
		continue
	if Option == 1:
		print("Balance GH: ", balance)
	if Option == 2:
		print("Balance GH: ", balance)
		withdraw = float(input("Enter Withdraw amount GH: "))
		if withdraw > 0:
			forewardbalance = (balance - withdraw)
			print("Foreward Balance GH: ", forewardbalance)
		elif withdraw > balance:
			print("No funs in account")
		else:
			print("None withdraw made")
	if Option == 3:
		print("Balance GH: ", balance)
		Deposit = float(input("Enter deposit amount GH: "))
		if Deposit > 0:
			forewardbalance = (balance + Deposit)
			print("Forewardbalance GH: ", forewardbalance)
		else:
			print("None deposit made")
	if Option == 4:
		exit()

