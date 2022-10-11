import rsa
file = open('pub_Bogomazov.key', 'r')
text = file.read()
pubkey = rsa.PublicKey._load_pkcs1_pem(text)
file.close()

message = "это зашифрованный текст".encode('utf-8')

encr_text = rsa.encrypt(message, pubkey)

encr_message = open("encr.msg", "wb")
encr_message.write(encr_text)
encr_message.close()