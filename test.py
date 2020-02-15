
def login():
	with open ('username.txt', 'r') as x:
		text = x.read()
		x.close()

	with open ('password.txt', 'r') as y:
		text1 = y.read()
		y.close()


	Login1 = input('Do you want to login or Create Account: L or A').upper()
	if Login1 == 'L':
		u = input('Username: ')
		p = input('Password: ')
		if u in text and p in text1:
			print('Access Granted!')
		else:
			print('Nope!')

	elif Login1 == 'A':
		with open('username.txt', 'a+') as f:
			f.write(input('Create Username')+'\n')
			f.close()
		with open('password.txt', 'a+') as i:
			i.write(input('Create Password')+'\n')
			i.close()
	else:
		return login()

login()
