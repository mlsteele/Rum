from rum import Client

rum_player_server = Client("server","password")
if rum_player_server.authenticate():
    print "Autenticated as server"
    rum_player_server.send('isaac', {"command": "load", "songs":
                                     ["http://creativesmoke.com/imusic/files/7127b4444b4722b1417b2da5d97f2367.mp3"]})
else:
    print "Authentication failed"
