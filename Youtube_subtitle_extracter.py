from youtube_transcript_api import YouTubeTranscriptApi

data = YouTubeTranscriptApi.get_transcript("m67gOMTkD_Y")

for i in data:
    print(i.get('text'))
