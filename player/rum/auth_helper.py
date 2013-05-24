import hashlib
RANDOM = "bzzfovHFWhD0wInhD8pEqXyVlrIIm3JK5VxEuXBu6B5ROmHec8AJ1yS5YgA4kkv"     

def sign_nonce(nonce, secret):
    return hashlib.sha256(nonce + secret).hexdigest()
def make_nonce():
    f = open("/dev/urandom")
    seed = f.read(100)
    f.close()
    return hashlib.sha256(seed).hexdigest()
def make_iv():
    return make_nonce()[0:16]
def make_key(secret):
    return sign_nonce(secret, RANDOM)[0:16]


INTERRUPT = "'"
PAD =  "\""

# Since you need to pad your data before encryption, 
# create a padding function as well
# Similarly, create a function to strip off the padding after decryption
def add_padding(data, block_size, interrupt=INTERRUPT, pad=PAD):
    new_data = ''.join([data, interrupt])
    new_data_len = len(new_data)
    remaining_len = block_size - new_data_len
    to_pad_len = remaining_len % block_size
    pad_string = pad * to_pad_len
    return ''.join([new_data, pad_string])
def strip_padding(data, interrupt=INTERRUPT, pad=PAD):
    return data.rstrip(pad).rstrip(interrupt)


