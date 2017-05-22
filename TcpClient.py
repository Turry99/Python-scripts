import socket

def Main():
	host = '192.168.0.103'
	port = 4000
	s = socket.socket()
	s.connect((host, port))

	message = input("-> ")
	while message != 'q':
		s.send(message.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		print("De la bebi: {}".format(data))
		message = input("-> ")
	s.close()

while __name__ == '__main__':
	Main()
