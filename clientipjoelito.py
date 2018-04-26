import socket
import threading
import sys
import pickle

class Cliente():
	
	"""docstring for Cliente"""
	def __init__(self, host="83.35.226.66", port=1980):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()
		nombre = input("Tu apodo: ")
		nombre1 = nombre.upper()
		while True:

			dd = print("--"+nombre1+"--")
			msg1 = input('->')

			
			
			if msg1 != 'salir':
				self.send_msg(dd+msg1)
			else:
				self.sock.close()
				sys.exit()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))


c = Cliente()