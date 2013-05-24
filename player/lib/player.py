import time, sys 
import rum_client as rum
from  VLCPlayer import Player




if len(sys.argv) == 2:
    NAME = sys.argv[1]
else:
    NAME = 'isaac'
    print "Usage: python bemix.py nodename"

player = Player()
r = rum.RumClient("isaac", "pete")
if r.authenticate():
    print "Authenticated"
else:
    print "auth failed"

def parse_server_update(update):
    for song in update.songs:
        player.load_url(song.url)
    player.unload()

    if song != None:
        if res['state'] == 'playing':
            player.play()
        elif res['state'] == 'paused':
            player.pause()

r.register_server_callback(parse_server_update)
r.setDaemon(True)
r.start()


while True:
    time.sleep(.1)

