import bluetooth

server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server.bind(("", 1))
server.listen(1)

client, address = server.accept()
print("Accepted conection from ", address)

try:
    while True:
	data = client.recv(1024)

        if data:
            print(data)
            client.send("well hello")
except:
    print("Closing connection")
    server.close()
    client.close()
