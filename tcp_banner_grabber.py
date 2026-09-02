import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target_ip = "127.0.0.1"
target_port = 8080

s.connect((target_ip, target_port))
print(f"Successfully connected to : {target_ip} on port : {target_port}")

banner_bytes = s.recv(1024)
banner_string = banner_bytes.decode('utf-8')

print("Banner Received : ")
print(banner_string)