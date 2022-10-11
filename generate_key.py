import rsa
(pubkey, privkey) = rsa.newkeys(2048)

priv_file = open('priv_Bogomazov.key','w')
priv_file.write(privkey._save_pkcs1_pem().decode())
priv_file.close()

pub_file = open('pub_Bogomazov.key', 'w')
pub_file.write(pubkey._save_pkcs1_pem().decode())
pub_file.close()