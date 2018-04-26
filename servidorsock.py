import socketserver

class mitcphandler(socketserver.BaseRequestHandler):
	def handler(self):
		self.oracion=self.request.recv(1024).strip()
		self.num=len(self.oracion)
		print ("La oracion recibida es",self.oracion,"el num de chars",self.request.send(self.num))

def main():
	print("Tutorial 53 Servidores")
	host=62.117.240.135
	port=9999
	server1 = socketserver.tcpserver((host,port),mitcphandler)
	print("server corriendo")
	server1.serve_forever()

main()
