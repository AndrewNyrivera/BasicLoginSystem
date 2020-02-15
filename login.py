def login():
	print('Login?')
	loggy = input('Do you want to login or make account. L or A').upper()
	if loggy == 'L':
		f = open('username.txt','r+')
		text = f.write(input('Username: '))
		x = open('password.txt','r+')
		text = f.write(input('Password: '))

		if 
	elif loggy == 'A':
		return 'A'
	else:
		return login()


	f = open('username.txt','r+')
	text = f.write(input())
	print(text)

	f.close()
print(login())