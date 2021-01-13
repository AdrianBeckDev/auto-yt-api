# Hi I am PyCutter 0.01                   #
# I cut and upload videos for lazy people #
# I'm developed by @adrianbeckdev @github #

from daytime import daytime
from moviepy.editor import *
from googleapiclient.discovery import build
from googleapiclient.discovery import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

import pytube
import requests
import selenium
import re
import os 
import json




#Global variables
#api_key= os.envrion.get('YT_API_KEY')
API_KEY= '<YOUR-API-KEY>'
youtube_api =build('youtube', 'v3', developerKey=API_KEY)
playlist_id = 'PLKeLOVL9lnYdBlniQK-3njHosocnNv8Rk'
videos = [] 
video_endcard_path = ''

#youtubeupload
CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES =['https://www.googleapis.com/auth/youtube.force-ssl']
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_console()

#Seleniumstuff





##request Login

request_body = {
    'snippet': {
        'categoryI': 19,
        'title': 'Upload Testing This is Private Video ',
        'description': 'Upload TEsting This is Private Video',
        'tags': ['Python', 'Youtube API', 'Google']
    },
    'status': {
        'privacyStatus': 'private',
        'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False,
    },
    'notifySubscribers': True
}






def get_yt_video():
    
    ##Searching for most popular Videos
    nextPageToken = None
    run = True
    
    while run:
        pl_request= youtube.playlistItems()list(
                part='contentDetails',
                playlistId=playlist_id,
                maxresults=50,
                pageToken=nextPageToken
         )
        pl_response = pl.request.execute()

        vid_id[]

        for item in pl_response['items']:
            vid_ids.append(item['contentDetails']['videoId']

        vid_request= youtube.videos().list(
            part = 'statistics'
            id =','.join(vid_ids)
        )

        for item in vid_response['items']:
            vid_views= item['statistics']['viewCount']
            vid_id =item['id']
            yt_link = f'https://youtu.be/{vid_id}'

            videos.append(
                {
                    'views': int(vid_views)
                    'url': yt_link
                }
            )
    
        nextPageToken= pl_response.get('nextPageToken')
        
        if not nextPageToken:
            break

        videos.sort(key=lambda vid: vid['views'], reverse = True)


        ##Download those videos

        for video in videos[:10]
            pytube.Youtube(vid['url']).streams.filter(only_audio=True).all()

    

    return 0 



def upload_to_beat_visualizer():
    #Trying to accomplish that  completely with selenium, but maybe there will be bot protection issues.
    #TRY: randomize/Captchasolver
    

    






    return 0




def download_from_beatvisalizer():
    return 0





def cut_yt_video():
    #add video from hendrik 
    #bassboost video 

    return 0





def upload_final():
    
    upload_date_time = datetime.now()
    
    mediaFile = MediaFileUpload('*.mp4')

    
    response_upload = youtube.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
    ).execute()
    
    """  
    youtube.thumbnails().set(
    videoId=response_upload.get('id'),
    media_body=MediaFileUpload('thumbnail.png')
    ).execute()
    """

    ##TODO
    ## get specific video id 

    return 0









