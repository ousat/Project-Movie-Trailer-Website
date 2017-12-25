'''
    This file has the module search which takes a search text as a parameter
    and returns the first result's video url from youtube
'''

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# developerkey obtained from google projects
DEVELOPER_KEY = 'AIzaSyCI3N0Qm5nOZ6JPj9QWCp6xq8Y_6sDzVhs'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def search(search_text):
    # the url without the videoid
    url = "https://www.youtube.com/watch?v="

    # youtube creates a google client object where service = youtube
    # read google api client documentation,
    # link provided in README for more info
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # search_response saves the result of youtube search query
    search_response = youtube.search().list(q=search_text,
                                            part='id,snippet',
                                            maxResults=1
                                            ).execute()
    # looping through the response
    for search_result in search_response.get('items', []):
        # checking if the result is a video
        if search_result['id']['kind'] == 'youtube#video':
            # appending the videoId to the rest of the url
            url += search_result['id']['videoId']

    return url
