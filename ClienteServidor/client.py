#!/usr/bin/python
import socket #importa a biblioteca socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criar um objeto socket TCP
host = socket.gethostname() #pega o nome da maquina loca
port = 60000 #reserva a porta 60000 para o servico

s.connect((host,port))
s.send("Ola servidor!")

with open('arquivo_recebido','wb') as f:
	print 'Abrindo o arquivo'
	while True:
		print('Recebendo os dados ...')
		data = s.recv(1024)
		print ('data = %s',data)
		if not data:
			break
		#escreve os dados no arquivo
		f.write(data)
f.close()
print('O arquivo foi baixado com sucesso')
s.close()
print('Conexao encerrada!')
