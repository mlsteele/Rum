from rum_auth_server import AuthServer
from player_server import PlayerServer
from client import Client
import time

clients_by_name = {"isaac"  : Client("isaac", "pete"), 
                   "pete"   : Client("pete","pete"),
                   "bemis"   : Client("pete","pete"),
                   "server" : Client("server", "password")}

if __name__ == '__main__':
    rum_auth_server = AuthServer(clients_by_name)
    rum_auth_server.setDaemon(True)
    rum_auth_server.start()
    
    rum_player_server = PlayerServer(rum_auth_server)
    rum_player_server.setDaemon(True)
    rum_player_server.start()


    while True:
        time.sleep(.1)
