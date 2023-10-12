import socket
import sys

port = 2500

# 서버 소켓 생성
s_sock = socket.socket()
host = ''

# 연결대기
s_sock.bind((host, port))
s_sock.listen(1)
print("Waiting for connection")


# 클라이언트로 부터 메시지 수신 및 출력
c_sock, addr = s_sock.accept()
print("connection from", addr)

msg = c_sock.recv(1024)
print(msg.decode())

# 클라이언트로 부터 파일 이름 입력 받기
filename = input("파일이름")

# 클라이언트에 파일 이름 전송
c_sock.send(filename.encode())

# 파일 열어서 전송
with open("./dummy/" + filename, 'rb') as f:
    c_sock.sendfile(f,0)

print('Sending Complete')
c_sock.close()
