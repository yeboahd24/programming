#!usr/bin/env/python3

#HTTP STATUS CODE

def status_code_meaning(number):
	if number == 200:
		return "OK"
	elif number == 301:
		return "Moved Permenantly"
	elif number == 401:
		return "Unauthorized"
	elif number == 404:
		return "Not Found"
	elif number == 500:
		return "Internal Sever Error"


#Using Hash Table

STATUS_CODES = {200: "OK", 301: "Moved Permenantly",
                401: "Unauthorized", 404: "Not Found",
                500: "Internal Server Error"

}
	

def status_code(number):
	return STATUS_CODES[number]

#Test Case:
data = 200
# print(status_code(data)) #OK



