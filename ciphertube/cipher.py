# 2022-04-22 Kiri, All rights reserved.
from typing import List

CIPHER_CLIENT_VERSION = '2.20220420.01.00'
CIPHER_SIGNATURE_TIMESTAMP = 19102

class Cipher:
    def __init__(self, s: str, sp: str, url: str):
        self.s = s
        self.sp = sp
        self.url = url
        self._deciphered_url = None
    
    def splice(self, target: List[str], amount: int):
        target = target[amount:]
    
    def swap(self, target: List[str], amount: int):
        target[0], target[amount % len(target)] = target[amount % len(target)], target[0]

    def reverse(self, target: List[str], amount: int):
        target.reverse()

    def decipher(self):
        target = list(self.s)
        self.reverse(target, 74)
        self.splice(target, 1)
        self.reverse(target, 32)
        self.swap(target, 65)
        self.reverse(target, 37)
        self.splice(target, 3)
        self.reverse(target, 66)
        self.s = ''.join(target)

    def decipher_all(self):
        self.decipher()
        self.s = self.s[:-4]

    @property
    def deciphered_url(self) -> str:
        if self._deciphered_url is None:
            self._deciphered_url = (
                self.url +
                '&'
                f'{self.sp}={self.s}'
            )
        return self._deciphered_url