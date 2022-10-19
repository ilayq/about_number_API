from hashlib import sha256
from datetime import date


def generate_api_key(user_name: str) -> str:
    to_hash = str(date) + user_name
    hash_ = sha256(to_hash.encode('utf-8'))
    with open('apikeys.txt', 'a') as f:
        f.write(hash_.hexdigest() + '\n')
    return str(hash_.hexdigest())
