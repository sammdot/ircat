#!/usr/bin/python3

import socket
import sys

def connect(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1800)
	try:
		sock.connect((host, port))
		return sock
	except socket.error as e:
		sys.stderr.write(e + "\n")

def send(sock, msg):
	sock.sendall(bytes(msg + "\r\n", "UTF-8"))

def listen(sock, callback):
	f = sock.makefile("rb")
	while True:
		msg = f.readline().decode("utf-8", errors="ignore").rstrip("\r\n")
		print(msg)
		parts = msg.split(" ")
		parts = parts[1:] if parts[0].startswith(":") else parts
		cmd = parts[0]
		if cmd == "PING":
			send(sock, "PONG " + parts[1])
		elif cmd == "ERROR":
			exit(0)
		elif cmd == "001":
			callback()

def main():
	pass
