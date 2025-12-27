import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
 
key = os.urandom(16)

nonce = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
encryptor = cipher.encryptor()
clair = b"Bonjour, a ce jour je n ai toujours pas recu vos identifiants pour finaliser votre inscription. Pouvez-vous me les envoyer ?"
ct = encryptor.update(clair) + encryptor.finalize()
decryptor = cipher.decryptor()
pt = decryptor.update(ct) + decryptor.finalize()

cipher2 = Cipher(algorithms.AES(key), modes.CTR(nonce))
encryptor2 = cipher2.encryptor()
clair2 = b"MESSAGEATROUVER"
ct2 = encryptor2.update(clair2) + encryptor2.finalize()
decryptor2 = cipher2.decryptor()
pt2 = decryptor2.update(ct2) + decryptor2.finalize()

print("Nonce :")
print(nonce.hex())
print("Chiffré envoyé")
print(ct.hex())

print("Chiffré répondu")
print(ct2.hex())

#Nonce :
#d548594b062fa5698e40ecad912b44bf
#Chiffré envoyé
#e714e538d8749a521074902a1db2e56b8606b7cd79570d67751ac3c8c2f11b80336a677d9c5e7c3be82aecba4fea1ade278084a3a50145c10ef4fb5def37537b886596f5b2041911fa00f1cb641d9c42afb1639f901ef3d362b15e706673764e698afef69c39916c93deb36df3d2dac090f43a6485fc48b285aaab7a
#Chiffré répondu
#ea0ee27e9771890d1071d56908e0e0669f11fac230570e287a538dc9c0e10380667c717daf5e7d6fff6fd9a61bfd19c8278c93b2eb19498755b5ac1abc271434ca2f96a7e858584da242b48f7d45d37cb8f435998b1eb0cb64a8446a297c2d1d4a8cabed9863df7b8edfa56dd7d39fc281ee6e64cbef49eb90bced





