# 2022-04-22 Kiri, All rights reserved.
CLIENT_LANG = 'ko'
CLIENT_NAME = 'WEB'
CLIENT_VERSION = '2.20220420.01.00'
SIGNATURE_TIMESTAMP = 19102

CLIENT_YOUTUBE_KEY = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'

CLIENT_FORMAT_DICT = {
    'client': {
        'hl': CLIENT_LANG,
        'clientName': CLIENT_NAME,
        'clientVersion': CLIENT_VERSION
    }
}

CLIENT_CONTEXT_BODY = {
    'context': CLIENT_FORMAT_DICT,
    'playbackContext': {
        'contentPlaybackContext': {
            'signatureTimestamp': SIGNATURE_TIMESTAMP
        }
    }
}