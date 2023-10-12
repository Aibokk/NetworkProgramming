import socket

s_socket = socket.socket()
host = "localhost"
port = 2500

# connection server
s_socket.connect((host, port))

# 메시지 전송
msg = "I am ready"
s_socket.send(msg.encode())

#서버로 부터 파일이름 수신
fn = s_socket.recv(1024).decode()

# 파일을 "recv"라는 이름으로 현재 디렉토리에 저장
with open("./dummy/" + "recv", 'wb') as f:
    print("Receiving")
    while True:
        data = s_socket.recv_fds(8192)
        if not data:
            break
        f.write(data)

print("Download complete")
s_socket.close()