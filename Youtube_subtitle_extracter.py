from youtube_transcript_api import YouTubeTranscriptApi
import time

id = input("Paste link of video:- ").split("/")
data = YouTubeTranscriptApi.get_transcript(id[len(id) - 1])

subtitle = ""
for i in data:
    subtitle += i.get('text') + " "

#print(subtitle)
file = open("subtitle.txt", 'w')
file.write(subtitle)
file.close()
print("Done")
time.sleep(2)

