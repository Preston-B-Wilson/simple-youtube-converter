import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainScreen(GridLayout):

    cwd = os.getcwd()

    last_text_input = ""
    all_text_input = []
    kivy_text_output = StringProperty("")

    current_dl_dir = cwd
    kivy_dir_output = StringProperty(cwd)

    def delete_queue(self):
        self.last_text_input = ""
        self.all_text_input = []
        self.kivy_text_output = ""

    def add_to_queue(self):
        input_txt = self.ids.my_text_input

        if input_txt.text == "":
            self.ids.url_warning.text = "Cannot enter empty url"
            return
        else:
            self.ids.url_warning.text = ""

        self.last_text_input = input_txt.text
        input_txt.text = ""

        self.all_text_input.append(self.last_text_input)
        reconstructed_text = ""

        for url in self.all_text_input:
            reconstructed_text += url + "\n"

        self.kivy_text_output = reconstructed_text

    def update_dl_dir(self):
        self.current_dl_dir = self.ids.my_text_input2.text
        self.ids.my_text_input2.text = ""
        self.kivy_dir_output = self.current_dl_dir

    def revert_dl_dir(self):
        self.current_dl_dir = self.cwd
        self.kivy_dir_output = self.cwd 

class SimpleYTConverterApp(App):
    pass

SimpleYTConverterApp().run()