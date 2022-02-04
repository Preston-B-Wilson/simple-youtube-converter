import os
import re
import asyncio
import pydub
from pytube import YouTube

cwd = os.getcwd()
yt = YouTube('hhttps://youtu.be/bBoRI1VJqFc')
og_path = "string"
new_path = "string"
title_mp4 = "string"
title_wav = "string"

stream = yt.streams.get_by_itag(139)

def title_scrubber(title):

    bad_characters = ['<', '>', ':', '"', "/" , "\\", '?', '*']
    bad_words = ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8",
        "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]
    
    for character in bad_characters:
        title = title.replace(character, '')

    for word in bad_words:
        title = re.sub(word, "", title)

    title = title.replace(' ', '_')

    return title


title = title_scrubber(yt.title)
title_mp4 = title + ".mp4"
title_wav = title + ".wav"

async def stream_download():

    stream.download(output_path=cwd, filename=title + ".mp4")
    
    while True:

        global og_path
        global new_path

        og_path = cwd + "\\" + title_mp4
        new_path = cwd + "\\" + title_wav

        if os.path.exists(og_path):
         
            break

    return cwd + title + ".mp4"
    

async def convert_to_wav():

    await asyncio.gather(stream_download())

    src = pydub.AudioSegment.from_file(og_path, "mp4")

    src.export(new_path, format="wav")


asyncio.run(convert_to_wav())


