import rsa
file = open('pub_Bogomazov.key', 'r')
text = file.read()
pubkey = rsa.PublicKey._load_pkcs1_pem(text)
file.close()
message = "Если вы это читаете, то это зашифрованный текст".encode('utf-8')

encrypt_text = rsa.encrypt(message, pubkey)

file = open('priv_Bogomazov.key', 'r')
text = file.read()
privkey = rsa.PrivateKey._load_pkcs1_pem(text)
file.close()

decrypt_text = rsa.decrypt(encrypt_text, privkey).decode()

#decr_text = rsa.encrypt(encr_text, privkey).decode('utf-8')

print(encrypt_text)
print(decrypt_text)