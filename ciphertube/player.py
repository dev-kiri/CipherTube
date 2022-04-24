# 2022-04-22 Kiri, All rights reserved.
import requests
from typing import List, Dict, Any
from ciphertube.stream import Stream
from ciphertube.client import CLIENT_YOUTUBE_KEY, CLIENT_CONTEXT_BODY

_PROTOCOL_HTTP = 'http://'
_PROTOCOL_HTTPS = 'https://'

_YOUTUBEI_DOMAIN = 'youtubei.googleapis.com'
_YOUTUBEI_PATH = '/youtubei/v1/player'

_YOUTUBEI_URL = _PROTOCOL_HTTPS + _YOUTUBEI_DOMAIN + _YOUTUBEI_PATH

class Player:
    def __init__(self, video_id: str):
        self.video_id = video_id
        self._video_info = None
        self._title = None
        self._formats = None
        self._streams = None

    @property
    def video_info(self) -> Dict[str, Any] | None:
        if self._video_info is None:
            res = requests.post(_YOUTUBEI_URL, params=dict(key=CLIENT_YOUTUBE_KEY), json=dict(**CLIENT_CONTEXT_BODY, video_id=self.video_id))
            self._video_info = res.json()
        return self._video_info
    
    @property
    def title(self) -> str | None:
        if self._title is None:
            res = self.video_info
            if 'videoDetails' in res:
                self._title = res['videoDetails']['title']
        return self._title

    @property
    def formats(self) -> List[Dict[str, str | int | Dict[str, str]]] | None:
        if self._formats is None:
            res = self.video_info
            if 'streamingData' in res:
                formats = []
                if 'formats' in res['streamingData']:
                    formats += res['streamingData']['formats']
                if 'adaptiveFormats' in res['streamingData']:
                    formats += res['streamingData']['adaptiveFormats']
                if len(formats) > 0:
                    self._formats = formats
        return self._formats

    @property
    def streams(self) -> List[Stream] | None:
        if self._streams is None:
            formats = self.formats
            title = self.title
            if formats is not None:
                streams = []
                for format in formats:
                    quality = None
                    itag = int(format['itag'])
                    mimeType = format['mimeType'].split(';')[0]
                    codecs = format['mimeType'].split('"')[1]
                    if 'qualityLabel' in format:
                        quality = format['qualityLabel']
                    elif 'quality' in format:
                        quality = format['quality']
                    if 'url' in format:
                        url = format['url']
                        streams.append(Stream(itag=itag, mimeType=mimeType, codecs=codecs, quality=quality, title=title, url=url))
                    elif 'signatureCipher' in format:
                        signature = format['signatureCipher']
                        streams.append(Stream(itag=itag, mimeType=mimeType, codecs=codecs, quality=quality, title=title, signature=signature))
                self._streams = streams
        return self._streams
    
    def stream(self, itag: int) -> Stream | None:
        for stream in self.streams:
            if stream.itag == itag:
                return stream