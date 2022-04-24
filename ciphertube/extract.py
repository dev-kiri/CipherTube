# 2022-04-22 Kiri, All rights reserved.
# http://stackoverflow.com/a/7936523/617185 
# Mikhail Kashkin(http://stackoverflow.com/users/85739/mikhail-kashkin)
# https://gist.github.com/kmonsoor/2a1afba4ee127cce50a0
from urllib.parse import urlparse, parse_qs

class Extract:
    def __init__(self, url: str):
        self.url = url
        self._video_id = None

    @property
    def video_id(self):
        """Returns Video_ID extracting from the given url of Youtube
    
        Examples of URLs:
          Valid:
            'http://youtu.be/_lOT2p_FCvA',
            'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
            'http://www.youtube.com/embed/_lOT2p_FCvA',
            'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
            'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
            'youtube.com/watch?v=_lOT2p_FCvA',
      
          Invalid:
            'youtu.be/watch?v=_lOT2p_FCvA',
        """
        if self._video_id is None:
            if self.url.startswith(('youtu', 'www')):
                self.url = 'https://' + self.url

            query = urlparse(self.url)
            
            if 'youtube' in query.hostname:
                if query.path == '/watch':
                    self._video_id = parse_qs(query.query)['v'][0]
                elif query.path.startswith(('/embed/', '/v/')):
                    self._video_id = query.path.split('/')[2]
            elif 'youtu.be' in query.hostname:
                self._video_id = query.path[1:]
                
        return self._video_id
