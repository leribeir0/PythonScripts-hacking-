#!/usr/bin/python
import socket
import sys
import re

file = open('lista.txt')
for linha in file.readlines():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((sys.argv[1],25))
	resp = s.recv(1024)
	s.send("VRFY "+ linha)
	resp = s.recv(1024)
	if re.search('252',resp):
		print "Usuario encontrado: " +resp.strip('252 2.0.0')