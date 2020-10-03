#!/usr/bin/env python
# coding: utf-8

# install all the packages

import os
import gc

# automatic garbage collection
gc.enable()
# https://pypi.org/project/pytube/
from pytube import YouTube 
from youtubesearchpython import SearchVideos
from datetime import datetime
from ast import literal_eval

# folder location : from where do you want to store the videos
folder_location = str(input("where do you want to download videos : "))
os.chdir(folder_location)

# change the no_of_videos_to_download from 2 to how many videos you want to download for any keyword
no_of_videos_to_download = 2

def download_file(video_link, keyword):
    """
    Function Description :  Function reads the parameters and download file into proper folder structure
    video_link : Link of the video from YouTube to download
    keyword : The keyword to which the video_link belongs to 
    """

    # create YouTube class object using the video_link paramter and chooses first stream response
    youtube_object = YouTube(video_link).streams.first()

    # check if the keyword folder exists or not
    if not os.path.isdir(keyword):
        # if not create the folder structure
        os.mkdir(keyword)

        # download the video in the folder
        youtube_object.download("./{}".format(keyword))
    else:

        # download the video in the folder
        youtube_object.download("./{}".format(keyword))

    # log to specify the video and the folder
    print("File saved successfully in Folder : {}".format(keyword))
    

def main(filename):
    """
    Function Description : Function read the filname in which the keywords are written
    filename : file in which the keywords are written
    """

    # read all the keywords in a file
    keywords = [keyword.strip() for keyword in open(filename).readlines()]
    # create a new temporary dictionary to store the videos with respect to their keywords
    keyword_dict = dict()

    # loop over the keywords to extract the video link to download
    for key in keywords:
        # create search object to class SearchVideos with parameter "max_results" which specifies how many videos to download, can be customised
        search = SearchVideos(str(key), offset = 1, mode = "json", max_results = no_of_videos_to_download)
        # convert the string type search result to python dictionary format
        result = literal_eval(search.result())

        # extract the video link from the search result dictionary
        keyword_dict[key] = [r['link'] for r in result['search_result']]

    # loop over the keywords
    for key in keyword_dict.keys():
        print("Current key : ", key)
        #print(keyword_dict[key])

        # call download_file function to download the videos
        for video in keyword_dict[key]:
            download_file(video, key)

# enter the filename to the prompt in which keywords are written
filename = input("enter filename to parse : ")

# calling main function
start = datetime.now()
main(filename)
print("Total time taken for task : ", datetime.now() - start)





