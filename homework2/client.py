from socket import *
import filecmp
import time
serverName = 'localhost'                                                    # This device
serverPort = 12000                                                          
clientSocket = socket(AF_INET, SOCK_STREAM)                                 # Connects using internet, tcp protocol
option=input("Choose 1 to send a file to server, 2 to check your file:")    # Choice of sending/receiving file
clientSocket.connect((serverName, serverPort))                              # Connects to server
clientSocket.send(option.encode())                                          # Sends the information of type of operation to server
time.sleep(1)                                                               # Wait is added so that the messages sent will not conflict

if int(option) == 1:                                                        # Sending a file option:
    with open("client.txt", "r") as file:                                   # First, reads the file
        contents = str(file.read(1024))                                     # Converts the content into string
    file.close()                                                            # Closes the file
    clientSocket.send(contents.encode())                                    # Sends the contents of the file, encoded in binary format
    clientSocket.close()                                                    # Closes the socket

elif int(option) == 2:                                                      # Receiving a file option:
    filecheck=clientSocket.recv(1024).decode()                              # Receives the contents of the file in binary and decodes it
    with open("filecheck.txt", "w") as file:                                # Writes the received contents as a file 
        file.write(filecheck)                                               
    file.close()                                                            # Closes the file

    file1 = "client.txt"                                                    # To compare the contents of two files:
    file2 = "filecheck.txt"

    if filecmp.cmp(file1, file2, shallow=False):                            # Compares the contents of two files
        print("Transmission successful.")                                   # Two files are the same, successful
    else:
        print("Transmission failed.")                                       # Two files are different, error
    clientSocket.close()                                                    # Closes the socket