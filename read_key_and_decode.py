import rsa
file = open('priv_Bogomazov.key', 'r')
text = file.read()
privkey = rsa.PrivateKey._load_pkcs1_pem(text)
file.close()

encr_message = open("encr.msg", "rb")
mess = encr_message.read()

decr_mess = rsa.decrypt(mess, privkey).decode('utf-8')

print(decr_mess)