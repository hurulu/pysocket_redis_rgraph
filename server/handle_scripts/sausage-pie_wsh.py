# Copyright 2011, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import time,random
import redis
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


def web_socket_do_extra_handshake(request):
    # This example handler accepts any request. See origin_check_wsh.py for how
    # to reject access from untrusted scripts based on origin value.

    pass  # Always accept.


def web_socket_transfer_data(request):
   # length = {}
   # maxlength = 1000
   # key_list = ['instances','vcpus','vcpus_per_instance','users','tenants']
   # for i in key_list:
   #     key = 'sa:usage:' + i
   # 	length[i] = r.llen(key)
   # 	init_data = r.lrange(key,length[i]-maxlength,-1)
   #     print key
   # 	request.ws_stream.send_message(i+'::'+str(init_data), binary=False)
    hash_list = ['vcpus_by_org']
    for i in hash_list:
        key = 'sa:usage:' + i
        init_data = r.hgetall(key)
        print key
        request.ws_stream.send_message(i+'::'+str(init_data), binary=False)
    while True:
        #line = request.ws_stream.receive_message()
        #if line is None:
        #    return
        #if isinstance(line, unicode):
        #s = str(random.randint(20,30))
	s = [] 
	#for i in key_list:
	#	key = 'sa:usage:' + i
	#	newlength = r.llen(key)
	#	if newlength > length[i]:
	#		s = r.lrange(key,-1,-1)
	#		length[i] = newlength
	#		print i+'::'+str(s[0])
	#		request.ws_stream.send_message(i+'::'+str(s[0]), binary=False)
	#
        #	time.sleep(1)
	#Read data from Hash and send it
        for i in hash_list:
	    key = 'sa:usage:' + i
	    s = r.hgetall(key)
	    print i+'::'+str(s)
	    request.ws_stream.send_message(i+'::'+str(s), binary=False)
        time.sleep(20)
	
        #    if line == _GOODBYE_MESSAGE:
        #        return
        #else:
        #    request.ws_stream.send_message(line, binary=True)


# vi:sts=4 sw=4 et
