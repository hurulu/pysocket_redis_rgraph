
1, Redis is used as backend database, install redis-server first
	Under redisdb dir, there is a sample redis database dump.rdb
2, install python-redis, sudo apt-get install python-redis on ubuntu
3, Start websocket servers
	cd server
	./start.sh
4, Place web to you webserver's root then open http://host:port/ in your browser.

For more information go to http://code.google.com/p/pywebsocket/ and http://www.rgraph.net/
