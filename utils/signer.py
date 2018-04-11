import base64

from django.core.signing import TimestampSigner

signer = TimestampSigner()


def encrypt_data(plain_data):
    encrypted = signer.sign(plain_data)
    return base64.urlsafe_b64encode(encrypted.encode('utf-8')).decode('utf-8')


def decrypt_data(encrypted_data, max_age=50):
    verification_key = base64.urlsafe_b64decode(encrypted_data)
    return {
        'signed_data': verification_key.decode('utf-8'),
        'result': signer.unsign(verification_key.decode('utf-8'), max_age=max_age)
    }

