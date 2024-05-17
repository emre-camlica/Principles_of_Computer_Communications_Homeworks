from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)                                 # Connects using internet, tcp protocol
serverSocket.bind(('', serverPort))                                         # Binds the server socket to port
serverSocket.listen(1)                                                      # Only one client at a time can connect

while True:                                                                 # The server operates non stop
    connectionSocket, addr = serverSocket.accept()                          # The server accepts client
    print("Choose 1 to send a file to server, 2 to check your file:")       # Type of the operation
    option=int(connectionSocket.recv(1024).decode())                        # Type is sent by the client, converted to integer value

    if option == 1:                                                         # Client sending a file option:
        print("option 1 is chosen.")                                        
        contents = str(connectionSocket.recv(1024).decode())                # Receives and decodes the contents of the client file, then converts it into string
        with open("server.txt", "w") as file:                               # Writes the decoded file as a new file
            file.write(contents)
        file.close()
        connectionSocket.close()                                            # Closes the connection socket

    elif option == 2:                                                       # Client receiving a file option:
        print("option 2 is chosen.")                            
        with open("server.txt", "r") as file:                               # The server reads the file it has
            contents = str(file.read(1024))                                 # Converting the file contents to string
        file.close()                                                        # Closes the file
        connectionSocket.send(contents.encode())                            # The server encodes and sends the file contents to client
        connectionSocket.close()                                            # Closes the connection socket

    else:                                                                   # Error case for receiving the option
        print("error")                                                      
        connectionSocket.close()