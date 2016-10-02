import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('135.251.200.221', 80))

s.bind(('127.0.0.1', 9999))
s.listen(5)
print 'Waiting for connection...'