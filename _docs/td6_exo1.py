import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
 
keyhex = (os.urandom(4)).hex()
key2 = keyhex+keyhex+keyhex+keyhex
key = bytes.fromhex(key2)
nonce = bytes.fromhex("664fe0e9ac9277efa4d8e2c5870a836a")
print('Nonce =')
print(nonce.hex())
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
encryptor = cipher.encryptor()
ct = encryptor.update(b"Bonjour Monsieur, pouvez-vous ameliorer ma note ?") + encryptor.finalize()
decryptor = cipher.decryptor()
pt = decryptor.update(ct) + decryptor.finalize()

nonceReponse = os.urandom(16)
cipher2 = Cipher(algorithms.AES(key), modes.CTR(nonceReponse))
encryptor2 = cipher2.encryptor()
ct2 = encryptor2.update(b"MESSAGEATROUVER") + encryptor2.finalize()
decryptor2 = cipher2.decryptor()
pt2 = decryptor2.update(ct2) + decryptor2.finalize()

print("Chiffré envoyé")
print(ct.hex())
print("Nonce Réponse")
print(nonceReponse.hex())
print("Chiffré répondu")
print(ct2.hex())

#MESSAGES REELLEMENT TRANSMIS SUR LE
#Nonce =
#664fe0e9ac9277efa4d8e2c5870a836a
#Chiffré envoyé
#92fb9874844441baeccb27ec38621ddea3c8c715530097c7e6e841f3117ed1e2b78a6796d75356924e23d819a1dd41fef8
#Nonce Réponse
#7102906ef729a019f2f148d343ea7a35
#Chiffré répondu
#b1353e170c5f8fc018ba98bafaf8061baf2415619a8b7df1fcc14d57c9c727344d428e692320c60dfefaf5427abd8179d4641c3bca91d49b




