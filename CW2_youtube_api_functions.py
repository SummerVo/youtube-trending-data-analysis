# Script for function to query data from youtube api
import googleapiclient.errors
import numpy as np

# get channel info
def get_channel_info(api, list_channel_id):
    '''
    Get information of channels in the list_channel_id
    
    Input:
        - api: youtube api's info, we need to set this up in the notebook 
        - list_channel_id: list of channel_id of channels we want to get information from

    Output:
        - channel_info (list): a list of sublist, each sublist include: channel_id, title
                               and statistics information of that channel (view, subscriber count, video count)
    '''
    channel_info = []
    channel_response = api.channels().list(
                part= "snippet, statistics", 
                id=','.join(list_channel_id)
            ).execute()
    # some channel did not have country so I replace it by nan
    for channel in channel_response['items']:
        try: 
            channel_info.append([channel["id"],
                                channel['snippet']['title'],
                                channel['snippet']['country'],
                                channel["statistics"]["viewCount"],
                                channel["statistics"]["subscriberCount"],
                                channel["statistics"]["videoCount"]
                                ])
        except KeyError:
            channel_info.append([channel["id"],
                                channel['snippet']['title'],
                                np.nan,
                                channel["statistics"]["viewCount"],
                                channel["statistics"]["subscriberCount"],
                                channel["statistics"]["videoCount"]
                                ])

    return channel_info



def get_video_base_on_time_range(api, channel_id, start_time, end_time):
    '''
    Get a list of videos of a specific channel within a certain time range
    
    Input:
        - api: youtube api's info, we need to set this up in the notebook 
        - channel_id: the unique id of a channel
        - start_time: str  (e.g.'2023-09-09T00:00:00Z')
        - end_time:   str

    Output:
        - videos_of_a_channel: list of videos of a channel in the time range we choose
    '''
    videos_of_a_channel = []
    nextPageToken = None
    while True:
        search_response = api.search().list(
                                                    part='snippet',
                                                    channelId=channel_id,
                                                    publishedAfter= start_time,
                                                    publishedBefore= end_time,
                                                    q = '',
                                                    type = 'video',
                                                    maxResults=50,
                                                    pageToken=nextPageToken
                                                ).execute()


        for item in search_response['items']:
            videos_of_a_channel.append(item['id']['videoId'])

        # to get more all videos from a channel (if they have more than 50 videos)
        nextPageToken = search_response.get('nextPageToken')
        if not nextPageToken:
            break
    return videos_of_a_channel


def get_video_info(api, list_vid_id, keys_content = [], keys_snippet = [], keys_statistic = []):
    '''
    Note: maximum number of videos for 1 run = 50
    Get snippet and contentDetail of videos in the list_vid_id. Need to define which information needed by keys_content and keys_snippet.
    To know more about which properties you can collect, check this page: https://developers.google.com/youtube/v3/docs/videos#resource
        
    Input:
        - api: youtube api's info, we need to set this up in the notebook 
        - list_vid_id: list of unique video_id we want to collect information from
        - keys_content: list of information from contentDetails
        - keys_snippet: list of information from snippet
    Output:
        - list_vid_stat: final list with each sublist is information of 1 videos
    '''
    # Check the length of the list_vid_id
    if len(list_vid_id)>50:
        print("Number of videos excess limit of 50 videos")
        pass
        
    list_vid_stat = []
    # query information of videos - batch
    vid_request = api.videos().list(
            part= "contentDetails, snippet", 
            id=','.join(list_vid_id)
        )
    vid_response = vid_request.execute()
    
    # getting information from each video
    for video in vid_response["items"]:
        # getting values from video snippet
        dict_snippet = video["snippet"]
        video_info = [dict_snippet.get(key) for key in keys_snippet]

        # getting values from video content details
        dict_content = video["contentDetails"]
        video_detail = [dict_content.get(key) for key in keys_content]

        # getting values from video statistics
        dict_stats = video["statistics"]
        video_stats = [dict_stats.get(key) for key in keys_statistic]
        
        # combine information of 1 video into 1 list
        one_video_values = [video["id"]] + video_info + video_detail + video_stats
        # add it into the main list
        list_vid_stat.append(one_video_values)
        
    return list_vid_stat

# create a function to get most recent comments in a youtube video
def get_comment(api, video_id):
    '''
    Get comments from one video

    Input:
        - api: youtube api's info, we need to set this up in the notebook 
        - video_id: unique video_id of a video
    Output:
        -list_comment: includes many sublist, each sublist is a info of 1 comment belong to that video
    '''
    nextPageToken = None
    list_comment = []
    while True:
        request = api.commentThreads().list(
                    part="snippet",
                    videoId= video_id,
                    maxResults=100,
                    pageToken=nextPageToken
                )
        video_response = request.execute()
        
        for item in video_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            list_comment.append([
                                    comment['authorDisplayName'],
                                    comment['publishedAt'],
                                    comment['textOriginal']
                                ])
            
        nextPageToken = video_response.get('nextPageToken')
            
        if not nextPageToken:
                break

    return list_comment
    