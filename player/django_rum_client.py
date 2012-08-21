from rum import Client

rum_player_server = Client("server","password")
if rum_player_server.authenticate():
    print "Autenticated as server"
    rum_player_server.send('isaac', {"command": "load", "songs": ["http://pizortech.com/techno.mp3"]})
else:
    print "Authentication failed"
