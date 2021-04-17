# This project currently only downloads MP4 videos
# Importing library 
from pytube import YouTube as YT

# Download path
download_Path = 'C://Users//Vaibhav Saran//Downloads//'

# Get the YouTube video Link from user
Link = input("Enter the Link to the video: ")

# Create an object of Youtube class to access the functions needed to download the video
try:
    yt_obj = YT(Link) # Creates the object and passes the link through constructor
except:
    print("Object Creation Failed !!!!")

# Filetering the files with MP4 extention 
mp4_video = yt_obj.streams.filter(progressive=True, file_extension='mp4')
# Sorting by the resolution in descending order
yt_obj.streams.order_by('resolution')
yt_obj.streams.desc()
yt_obj.streams.first().download(download_Path)