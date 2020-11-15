import amino
import  socket
import time
import threading

host="127.0.0.1"
port=3332
client=amino.Client()
def Main():
	try:
		sock = socket.socket()
		sock.connect((host, port))
		email=input("Type email: ")
		password= input("Type Password: ")
		data=email,password
		data=str(data).encode("utf-8")
		sock.send(data)
		client.login(email=email ,password=password)
		comid=input("Type Forum ID: ")
		chatid=input("Chat Link: ")
		chatid=client.get_from_code(chatid).objectId
		subclient=amino.SubClient(comId=comid ,profile=client.profile)
		while True:
			try:
				masaage=input("Type Massage: ")
				subclient.send_message(message=massage ,chatId=chatid , messageType=110)
			except:
				pass
	except socket.error  as msg:
		print (msg)
		time.sleep(5)
		Main()
Main()
	