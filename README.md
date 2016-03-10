# http-server

### Client (client.py)

This file takes a message provided to the method client("your message") and transmits 
the contents to a server on a fixed IP:Port as provided in the client.py file.

Calling client() with no message will transmit the global test message, 
test_message = 'Worst case test message!'

### Server (server.py)

This file sets up and configures a localhost server to listen on a provided
IP:Port in the server.py file. The server will then receive and process valid
messages against it's known protocols and respond with a well formed response 
that includes the provided URI from the message message or a relevant
response code.