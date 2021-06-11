from cryptography.fernet import Fernet


# Fernet for obfuscation
def encrypt_user_details(username=None,name=None):
    encoded_username = username.encode()
    encoded_name = name.encode()

    '''
    the_secret_file = open('backend/key.txt','rb')
    key = the_secret_file.read().decode()
    print(key)
    the_secret_file.close()
    '''

    f = Fernet(b'aIuJ5qLfakZc-2YXDCr4MVVOBrLMebGKqKFU94R_bAQ=')
    encrypted_username = f.encrypt(encoded_username)
    encrypted_name = f.encrypt(encoded_name)
    return encrypted_username, encrypted_name


def encrypt_mail(username):
    encoded_mail = username.encode()
    print(encoded_mail)
    f = Fernet(b'aIuJ5qLfakZc-2YXDCr4MVVOBrLMebGKqKFU94R_bAQ=')
    encrypted_mail = f.encrypt(encoded_mail)
    return encrypted_mail


def decrypt_user_details(encrypted_username=None,encrypted_name=None):

    f = Fernet(b'aIuJ5qLfakZc-2YXDCr4MVVOBrLMebGKqKFU94R_bAQ=')
    decrypted_username = f.decrypt(encrypted_username)
    decrypted_name = f.decrypt(encrypted_name)

    decoded_username = decrypted_username.decode()
    decoded_name = decrypted_name.decode()

    return decoded_username, decoded_name
