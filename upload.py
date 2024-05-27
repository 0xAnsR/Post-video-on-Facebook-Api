# prompt: write a python script to upload video on meta using video url

import requests
import json

# Replace these values with your own
video_url = "https://example.com/video.mp4"
meta_access_token = "YOUR_META_ACCESS_TOKEN"
page_id = "YOUR_PAGE_ID"

data = {
    "access_token": meta_access_token,
    "message": "This is a test video",
    "source": video_url
}

url = f"https://graph.facebook.com/v2.11/{page_id}/videos"

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Video uploaded successfully")
else:
    print("Error uploading video:", response.text)
