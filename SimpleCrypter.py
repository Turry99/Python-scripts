#We first reverse the string and
#multiply by 4 and add 3 to the ord of the character
string = "Hi, my name is what?"
def Encrypt(string):
	new_string = ''
	string = string[::-1]
	for char in string:
		new_string += chr(ord(char)*4 + 3)
	return new_string
def Decrypt(string):
	new_string = ''
	for char in string:
		new_string += chr(int((ord(char)-3)/4))
	new_string = new_string[::-1]
	return new_string
if __name__ == '__main__':
	print("Encrypted string: {}".format(Encrypt(string)))
	print("Decrypt the encrypt function: {}".format(Decrypt(Encrypt(string))))
