# Cipher Hacker

message = 'guv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#loop through every possible key:

for key in range(len(SYMBOLS)):
	translated = ''

	#loop through each symbol in message:
	for symbol in message:
		if symbol in SYMBOLS:
			symbolIndex = SYMBOLS.find(symbol)
			translatedIndex = symbolIndex - key

			if translatedIndex < 0:
				translatedIndex = translatedIndex + len(SYMBOLS)

				#Append the decrypted symbol
			translated = translated + SYMBOLS[translatedIndex]

		else:
			translated = translated + symbol

		#Display every possible decrypion
	print(f'#{key}: {translated}')
		