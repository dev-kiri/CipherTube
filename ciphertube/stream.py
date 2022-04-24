# 2022-04-22 Kiri, All rights reserved.
import mimetypes
import requests
from tqdm import tqdm
from urllib.parse import urlsplit, parse_qsl

from ciphertube.cipher import Cipher

class Stream:
    def __init__(
        self,
        itag: int, 
        mimeType: str, 
        codecs: str, 
        quality: str, 
        title: str = None,
        url: str = None,
        signature: str = None
    ):
        self.itag = itag
        self.mimeType = mimeType
        self.codecs = codecs
        self.quality = quality
        self.title = title
        self._url = url
        self._signature = signature
    
    def __repr__(self) -> str:
        return (
            self.__class__.__qualname__ +
            f'(itag={self.itag!r}, '
            f'mimeType={self.mimeType!r}, '
            f'codecs={self.codecs!r}, '
            f'quality={self.quality!r})'
        )
    
    @property
    def signature(self):
        return self._signature
    
    @property
    def url(self):
        if self._url is None and self.signature is not None:
            data = dict(parse_qsl(urlsplit(self.signature).path))
            cipher = Cipher(s=data['s'], sp=data['sp'], url=data['url'])
            cipher.decipher_all()
            self._url = cipher.deciphered_url
        return self._url
    
    def download(self, chunk_size: int = 1024):
        ext = mimetypes.guess_extension(self.mimeType) or '.mp4'
        name = self.title + ext
        res = requests.get(self.url, stream=True)
        if res.status_code == 200:
            total = int(res.headers.get('Content-Length', 0))
            with open(name, 'wb') as file, tqdm(
                desc=name,
                total=total,
                unit='B',
                unit_scale=True,
                unit_divisor=1024
            ) as bar:
                for chunk in res.iter_content(chunk_size=chunk_size):
                    size = file.write(chunk)
                    bar.update(size)
        else:
            raise