from rum import Client

rum_player_server = Client("server","password")
if rum_player_server.authenticate():
    print "Autenticated as server"
    rum_player_server.send('isaac', {"command": "load", "songs":
                                     ["http://audio-sv5-t1-2.pandora.com/access/8094719601065360136.mp4?version=4&lid=2762360&token=0pBek51SvItVXt5G2u8saswbeHK%2BXdB55AmiYUEE5dNm38bpOO7JQ%2BFH1QFGGtcDD5VT0jJOfJN1lr7yApGhJT71Z5TU5YLwe3aSPBLh21784YiJT%2FdEAomleCZrmtjC7LL4SHS1sHgDCfUS9d652KsswcHVDKx3J8J9S9%2BDuuoTWqvTaABKF8Ezet3C2go4BqhRUG%2F9VoVyEDSRkR4v4W%2FSLL0UmfsAVaAVAm3yX4WCYj51m7zEuR2sEWfgEgv9xI6PjTHda8vKCDKisVXqg6Z4BYe1Svw%2Fjnj6pFzCVuk%2Beswfpf%2F9IMSyU1YBAUIktob1Mgf7fNarDQj3976aBaa%2BP5QPX3Rk"]})
else:
    print "Authentication failed"
