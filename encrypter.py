from cryptography.fernet import Fernet

key = Fernet.generate_key()
crypter = Fernet(key)

def locker(passwd: str):
    encrypted_stuff = crypter.encrypt(bytes(passwd, "utf8"))
    
    return encrypted_stuff

def unlocker(passwd: str):
    decrypted_stuff = crypter.decrypt(passwd)
    decrypted_stuff = str(decrypted_stuff, "utf8")
    
    return decrypted_stuff