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

def listen(sock):
	f = sock.makefile("rb")
	while True:
		msg = f.readline().decode("utf-8", errors="ignore").rstrip("\r\n")

def main():
	pass
