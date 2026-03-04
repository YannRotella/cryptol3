import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
 
keyhex = (os.urandom(4)).hex()
key2 = keyhex+keyhex+keyhex+keyhex

#permet de transformer une chaine en hexa en tableaux d'octets
key = bytes.fromhex(key2)

nonce = bytes.fromhex("664fe0e9ac9277efa4d8e2c5870a836a")
print('Nonce =')

#permet d'avoir un meilleur affichage qu'un tableau d'octets
print(nonce.hex())

#declaration du block cipher et du mode utilisé
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))

#objet à appeler
encryptor = cipher.encryptor()
ct = encryptor.update(b"Bonjour Monsieur, pouvez-vous ameliorer ma note ?") + encryptor.finalize()
decryptor = cipher.decryptor()
pt = decryptor.update(ct) + decryptor.finalize()

#Il faudra peut etre commenter ceci. Cela vous est donne pour vous aider
nonceReponse = os.urandom(16)
cipher2 = Cipher(algorithms.AES(key), modes.CTR(nonceReponse))
encryptor2 = cipher2.encryptor()
ct2 = encryptor2.update(b"MESSAGE A TROUVER") + encryptor2.finalize()
decryptor2 = cipher2.decryptor()
pt2 = decryptor2.update(ct2) + decryptor2.finalize()

print("Nonce")
print("Chiffré envoyé")
print(ct.hex())
print("Nonce Réponse")
print(nonceReponse.hex())
print("Chiffré répondu")
print(ct2.hex())

#les chiffres du prof et de l'etudiant
ct_prof = bytes.fromhex("4e63aacd834529d18f507c302c2fedb8d28e11d642b559292f4af9401b7464207351456227becd82f3d914ccbfbaa6427429329615ce86953a87eb7881e245d6fc5a16a8775531a3125156ca7a7bffc26448eeb138931047b676ce37bc879aae2f45bb841e2b9cd6513ce3be80f146d94489b48f5bf1218924227e11e20995da0adb3d71fb37a5ea1f70")
ct_etu = bytes.fromhex("9799bc41d104f0cb2255ea76791efe0fee40e08460d082577e4a78becf71e7c6c866e663ed8dd16ab007bcc150b96b2113")

#Une fonction utile ? si i est un entier, i.to_bytes(4, 'big') permet de trsnformer un entier en octets
n = 23974930
v = n.to_bytes(4,'big')
print(v)
print(v.hex())

#MESSAGES REELLEMENT TRANSMIS SUR LE CANAL
#Nonce =
#664fe0e9ac9277efa4d8e2c5870a836a
#Nonce
#Chiffré envoyé
#9799bc41d104f0cb2255ea76791efe0fee40e08460d082577e4a78becf71e7c6c866e663ed8dd16ab007bcc150b96b2113
#Nonce Réponse
#efa35dd810a74f9fb769239de9933f19
#Chiffré répondu
#4e63aacd834529d18f507c302c2fedb8d28e11d642b559292f4af9401b7464207351456227becd82f3d914ccbfbaa6427429329615ce86953a87eb7881e245d6fc5a16a8775531a3125156ca7a7bffc26448eeb138931047b676ce37bc879aae2f45bb841e2b9cd6513ce3be80f146d94489b48f5bf1218924227e11e20995da0adb3d71fb37a5ea1f70

