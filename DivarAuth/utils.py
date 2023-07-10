import random
from DivarCore.extenstion import redisServer

def generate_account_verify_token():
    """Generate a token for verify user account"""
    return random.randint(999_99+1, 999_999+1)

def generate_login_code():
    """Generate Unique Login Code For Each User"""
    while True:
        code = random.randint(999_99+1, 999_999+1)
        code = str(code)
        if redisServer.get(code):
            continue
        else:
            return str(code)
