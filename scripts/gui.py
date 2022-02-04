import os
import kivy
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

cwd = os.getcwd()
size = len(cwd)
cwd = cwd[:size - 8]

Builder.load_file(cwd + "/layouts/remixassistant.kv")


class RemixAssistant(BoxLayout):
    pass

class RemixAssistantApp(App):
    
    def build(self):
        return RemixAssistant()

if __name__ == '__main__':
    RemixAssistantApp().run()