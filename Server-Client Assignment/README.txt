Write a networked client/server application in Python which allows a client program to query a simple database which is managed by a server program. For this assignment we selected a database of NFL games as an example. The client program sends a message containing the query about a game to the server and the server program responds back with a message containing the requested information. Communications between the client and server must be secured using a hybrid encryption scheme in which asymmetric encryption is used to transmit a session key at the start of a session, and symmetric encryption is used for the remainder of the session.

1. Operation of the Client/Server
The application is actually two different programs, the client program and the server program. These two programs should both be running as two separate processes which are invoked by the user in a shell. These two programs may be running on the same machine but they may be running on two different machines.

 

The server must be started before the client. The server will listen to a port until a client initiates communication. Once communication has been initiated, the user will enter a request at the command line of the client, and the client will send that request to the server. The server will send a corresponding response to the client and the client will print the contents of that response on the screen for the user to see. This process will continue until the client sends a quit message to the server. Once the client sends a quit message, the client will quit and the server will wait for another client to initiate communication.

 

2. Game Data File
The server will need access to a database of information about NFL games. You will use a comma-separated value (csv) file to populate the server’s database. An example game data file can be found here, data_base.csv.csv  Download data_base.csv.csv. The first row of csv file is the name of each field and remains unchanged. It won't be read into the database. Other than the first line, each line contains information regarding a single game. Each row has the following 8 fields separated by commas.

 

type

game_id

home_team

away_team

week

season

home_score

away_score

 

type: specifies if this match was a regular or post season match. 
Possible values: [reg, post]
game_id: unique identifier for a specific match. 
Example: 2018122400
home_team: short name of home team for each match.
Examples: GB, NYJ  
away_team: similar to home_team but specifying the away team.
Examples: LA, KC  
week: week number in the season that match was held. 
Possible values: [1 to 20]
season: year that match belongs to. 
Examples: 2005, 2006, 2019
home_score: number of points home team scored in that match
Possible values: [0-1000]
away_score: number of points away team scored in that match
Possible values: [0-1000]
Sample:

 

type,game_id,home_team,away_team,week,season,home_score,away_score
reg,2018090600,PHI,ATL,1,2018,18,12
reg,2018090900,BAL,BUF,1,2018,47,3
reg,2018090907,NYG,JAX,1,2018,15,20
reg,2018090906,NO,TB,1,2018,40,48
reg,2018090905,NE,HOU,1,2018,27,20

3. User interface

User Interface of the Server

 

The server should be started before the client. The server program should take three command line arguments: 

Server Port - The number of the port which the server is listening to. 
Game Data File - The name of the file containing the database of all information about all games.
Private Key File - The name of the file containing the server’s private key. 
 

The Private Key File is a file whose only contents are the server’s private key. 

 

When the server is started, it should print “server started” and then wait to receive messages from a client. Only one client can connect to the server at a time. When the server receives a request from a client, the server will print the game_id and field in the message on the screen on a new line. An example of the printed output of the server when communicating with the client is shown below. 

 

server started

2018090600 game_id

2018090600 home_team

2018090600 away_team

2018090600 week

2018090600 season

2018090600 home_score

2018090600 away_score




The server will continue responding to requests from a client and printing the associated information until a quit message is received. At that point, the server will stop communicating with the client and wait for a new client to initiate communication. The server will continue to run in an infinite loop until its process is killed externally, for instance by a ctrl-c typed at the keyboard.

4. User Interface of the Client

The client program should take three command-line arguments:

Server Host - This is the host name on which the server program is running.
Server Port - This is the port number on the server host which the server is listening to.
Server Public Key File - This is the name of the file which contains the server’s public key.
 

The Server Public Key File is a file whose only contents are the server’s public key.

 

The client will present the user with a prompt, “>”. The user makes requests for game information by entering game_id and field info at the client’s prompt. When this information is entered at the client’s prompt, the client will send a data request message containing the game_id and field to the server, and the client will await a data response message from the server. The server will send a data response message containing the corresponding information of the field for the match with that game_id. The client will print the received information to the screen, print a prompt on a new line, and wait for more input from the user. An example of a user interaction with the client is shown below. 




> 2018090600 type

reg

> 2018090600 game_id

2018090600

> 2018090600 home_team

PHI

> 2018090600 away_team

ATL

> 2018090600 week

1

> 2018090600 season

2018

> 2018090600 home_score

18

> 2018090600 away_score

12

> whats up?

unknown

> 2018090600 away_score

12

> quit


The client will continue in this loop until the user enters “quit”, at  which point the client will send a quit message to the server and the client’s process will exit. 

5. Types of messages
 

There are 4 types of messages sent between the client and server.

 

Initiate Communication - This message is the first message sent from a client to a server in order to start a communication session. This message must be encrypted with an asymmetric cipher using the public key of the server. The contents of this message must be  random bytes which will serve as a session key to be used for symmetric encryption during the remainder of the communication session. The server will decrypt this message using its private key. The server will not generate a response to this message.
Data Request - This message is sent by the client in order to request data about a game from the server. Each data request message will contain two pieces of information, a string, and the length of the string. The string will be exactly the request string entered by the user: the game_id and field, separated by white space. The string will be prefixed by a header which contains the length of the string. Each message must be shorter than 256 bytes long and must be formatted as follows:
Byte 0: Length of the string
Bytes 1 – n: Characters of the string
Data Response - This message is sent by the server to provide information about a game. Each data response message will contain two pieces of information, a string, and the length of the string. The string will be the game information requested by the user. The string will be prefixed by a header which contains the length of the string. Each message must be shorter than 256 bytes long and must be formatted as follows:
Byte 0: Length of the string
Bytes 1 – n: Characters of the string
Quit Message - The quit message is sent by the client to end a communication session. Each quit message will contain two pieces of information, a string, and the length of the string. The string will be “quit”. The string will be prefixed by a header which contains the length of the string. The message must be formatted as follows:
Byte 0: Length of the string
Bytes 1 – n: Characters of the string
 

All messages of type Data Request, Data Response, and Quit Message must be encrypted using the session key. 

6. Implementation Details

If the game_id or the field typed into the client is not in the database which is known to the server, just return “unknown” and continue the program.
Don’t worry about invalid input typed into the client. Everything entered into the client can be assumed to be a valid input.
For any corner cases, you can use “unknown” for commands that do not fit the description of the assignment and “unknown” for any information requested that do not exist.
 