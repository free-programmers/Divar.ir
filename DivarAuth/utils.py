import random
from DivarCore.extenstion import redisServer

def generate_account_verify_token():
    """Generate a token for verify user account"""
    return random.randint(999_99+1, 999_999+1)