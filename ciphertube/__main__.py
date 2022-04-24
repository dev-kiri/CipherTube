# 2022-04-22 Kiri, All rights reserved.
from typing import List
from ciphertube.player import Player
from ciphertube.extract import Extract
from ciphertube.stream import Stream

class CipherTube:
    def __init__(self, url: str):
        self.url = url
        self._player = None
        self._title = None
        self._video_id = None
        self._streams = None

    @property
    def player(self) -> Player:
        if self._player is None:
            self._player = Player(video_id=self.video_id)
        return self._player

    @property
    def title(self) -> str | None:
        if self._title is None:
            player = self.player
            return player.title

    @property
    def video_id(self) -> str | None:
        if self._video_id is None:
            extract = Extract(url=self.url)
            self._video_id = extract.video_id
        return self._video_id

    @property
    def streams(self) -> List[Stream]:
        if self._streams is None:
            player = self.player
            self._streams = player.streams
        return self._streams

    def stream(self, itag: int) -> Stream | None:
        for stream in self.streams:
            if stream.itag == itag:
                return stream
    


