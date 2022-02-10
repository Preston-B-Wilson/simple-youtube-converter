import os, ytconvert, threading

from pytube import YouTube

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainScreen(GridLayout):

    cwd = os.getcwd()
    parent_dir = cwd[:-8]
    print(parent_dir)
    default_dl_dir = parent_dir + "\\downloads"
    dl_dir = default_dl_dir
    if not os.path.exists(dl_dir):
        os.mkdir(dl_dir)
    kivy_dir_output = StringProperty("Active download directory\n" + dl_dir)

    last_text_input = ""
    all_text_input = []
    kivy_url_output = StringProperty("")

    def delete_queue(self):
        self.ids.url_warning.text = ""
        self.last_text_input = ""
        self.all_text_input = []
        self.kivy_url_output = ""

    def add_to_queue(self):
        input_txt = self.ids.my_text_input

        if input_txt.text == "":
            self.ids.url_warning.text = "Cannot enter empty url"
            return
        elif not "https://www.youtube.com" in input_txt.text:
            self.ids.url_warning.text = "Invalid url"
            return
        else:
            self.ids.url_warning.text = ""

        self.last_text_input = input_txt.text
        input_txt.text = ""

        self.all_text_input.append(self.last_text_input)
        reconstructed_text = ""

        for url in self.all_text_input:
            yt_obj = YouTube(url)
            title = yt_obj.title
            reconstructed_text += title + "\n"

        self.kivy_url_output = reconstructed_text

    def update_dl_dir(self):
        input_dir = self.ids.my_text_input2
        if input_dir.text == "":
            self.ids.dir_warning.text = "Cannot enter empty directory"
            return
        elif not os.path.exists(input_dir.text):
            self.ids.dir_warning.text = "Directory does not exist"
            return
        else:
            self.ids.dir_warning.text = ""
        self.dl_dir = input_dir.text
        self.kivy_dir_output = "Active download directory\n" + self.dl_dir

    def revert_dl_dir(self):
        self.dl_dir = self.default_dl_dir
        self.ids.my_text_input2.text = ""
        self.ids.dir_warning.text = ""
        self.kivy_dir_output = "Active download directory\n" + self.dl_dir

    def goto_path(self):
        print(self.dl_dir + "\\")
        os.startfile(self.dl_dir)

    def run_download(self):
        thread1 = threading.Thread(target=ytconvert.YTConvert, args=(self.all_text_input, "wav", self.dl_dir, True))
        thread1.start()

class SimpleYTConverterApp(App):
    pass

SimpleYTConverterApp().run()