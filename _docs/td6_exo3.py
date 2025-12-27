import os
from cryptography.hazmat.primitives import hashes


digest = hashes.XOFHash(hashes.SHAKE128(digest_size=32))

digest.update(b"abc")
digest.update(b"123")
digest.squeeze(4)
digest.squeeze(4)