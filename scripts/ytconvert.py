import sys, os, re, threading, asyncio, pydub
from pytube import YouTube

class YTConvert:

    def __init__(self, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", custom_format = "wav", custom_dir = "nope" , self_run = False):

        if self_run == True:
            YTConvert(url, custom_format, custom_dir, False).run()
            sys.exit()

        if isinstance (url, list):
            self.threads = []

            for x, unique in enumerate(url, start=1):
                thread_name = f"thread{x}"
                thread_name = threading.Thread(target = YTConvert, args = (unique, custom_format, custom_dir, True))
                self.threads.append(thread_name)

            for thread in self.threads: thread.start()
            for thread in self.threads: thread.join()

            sys.exit()

        self.cwd = os.getcwd()

        if custom_format not in ["mp4", "wav"]:
            sys.exit("Invalid format. Please use mp4 or wav.")
        
        self.format = custom_format

        if (os.path.exists(custom_dir)):
            self.dl_dir = custom_dir
        elif (custom_dir == "nope"):
            self.dl_dir = self.cwd[:-8] + "\\downloads"
        else:
            sys.exit("Specified directory does not exist.")

        self.yt_url = url
        self.yt_obj = YouTube(self.yt_url)

        self.stream = self.yt_obj.streams.get_by_itag(139)

        self.title = self.title_scrubber(self.yt_obj.title)
        self.title_mp4 = self.title + ".mp4" 
        self.title_format = self.title + "." + self.format

        self.mp4_dl_path = self.dl_dir + "\\" + self.title_mp4
        self.new_format_path = self.dl_dir + "\\" + self.title_format

        self.mp4_exist = False

    def title_scrubber(self, title):

        bad_characters = ['<', '>', ':', '"', "/" , "\\", '?', '*']
        bad_words = ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8",
            "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]
        
        for character in bad_characters: title = title.replace(character, '')
        for word in bad_words: title = re.sub(word, "", title)
        title = title.replace(' ', '_')

        return title

    async def download_stream(self):

        if os.path.exists(self.mp4_dl_path):
            self.mp4_exist = True

        self.stream.download(output_path=self.dl_dir, filename=self.title_mp4)
       
        while not os.path.exists(self.mp4_dl_path): pass
        
    async def convert_to_format(self):

        src = pydub.AudioSegment.from_file(self.mp4_dl_path, "mp4")

        src.export(self.new_format_path, format=self.format)

    def run(self):   
        asyncio.run(self.download_stream())
        if self.format != "mp4": 
            asyncio.run(self.convert_to_format())
            if not self.mp4_exist: os.remove(self.mp4_dl_path)
        print("Successfully downloaded" + (" and converted " if self.format != "mp4" else " ")  + self.format + " of " + self.title)







