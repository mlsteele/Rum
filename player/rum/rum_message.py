import protocol.rum_message_pb2 as rum_message_pb2
import hashlib
import json
import auth_helper
from Crypto.Cipher import AES
class RumMessage(object):
    PLAIN = 'plain'
    SIGNED = 'signed'
    ENCRYPTED = 'encrypted'
    def __init__(self,
                payload = {},
                src = '',
                dst = 'server'):
        self.src = src
        self.crypto = ""
        self.dst = dst
        self.security = self.PLAIN
        self.payload = payload
        self._payload = json.dumps(payload)

    def _update_payload(self):
        if self.security == self.ENCRYPTED:
            self.payload = self._payload[:]

        else:
            self.payload = json.loads(self._payload)
    
    def parse_from_multipart(self, message):
        self.dst = message[0]
        self.src = message[1]
        self.security = message[2]
        self._payload = message[3]
        self.crypto = message[4]
        self._update_payload()

    def serialize_to_multipart(self):
        self._update_payload
        multipart = [self.dst, 
                     self.src,
                     self.security, 
                     self._payload,
                     self.crypto]
        
        return multipart

    def encrypt(self, secret):
        self.crypto = auth_helper.make_nonce()[0:16]
        key = auth_helper.make_key(secret)
        message_padded = auth_helper.add_padding(self._payload, 16)
        obj = AES.new(key, AES.MODE_CBC, self.crypto)
        self._payload = obj.encrypt(message_padded)
        self.security = self.ENCRYPTED
        self._update_payload()

    def decrypt(self, secret):
        key = auth_helper.make_key(secret)
        obj = AES.new(key, AES.MODE_CBC, self.crypto)
        message_padded  = obj.decrypt(self._payload)
        self._payload = auth_helper.strip_padding(message_padded)
        self.security = self.PLAIN
        self._update_payload()


    
    def _hashable(self):
        return ''.join(self.serialize_to_multipart()[0:3])

    def sign(self, secret, token):
        self.security = self.SIGNED
        self.crypto = hashlib.sha256(self._hashable() + 
                                    secret +
                                    token).hexdigest()
    def verify(self, secret, token):
        observed_sig = hashlib.sha256(self._hashable() + 
                                    secret +
                                    token).hexdigest()
        return observed_sig == self.crypto
        
if __name__ == '__main__':
    m = RumMessage({'name': 'main'}, "isaac", "server")
    print m.payload
    m.sign("pete","token")
    print m.verify("pete", "token")
    print m.serialize_to_multipart()
