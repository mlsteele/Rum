import time, sys 
from rum import Client
from  lib.VLCPlayer import Player




if len(sys.argv) == 2:
    NAME = sys.argv[1]
else:
    NAME = 'isaac'
    print "Usage: python bemix.py nodename"

player = Player()
r = Client("isaac", "pete")
if r.authenticate():
    print "Authenticated"
else:
    print "auth failed"

def parse_server_update(update):
    songs = update["songs"]
    player.load_url(songs[0])
    player.play()
    return
    player.unload()

    if song != None:
        if res['state'] == 'playing':
            player.play()
        elif res['state'] == 'paused':
            player.pause()

r.register_message_handler(parse_server_update)
r.setDaemon(True)
r.start()


while True:
    time.sleep(.1)
