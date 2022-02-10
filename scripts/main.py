from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainScreen(GridLayout):

    text_input_str = StringProperty("")

    def delete_queue(self):
        self.text_input_str = ""

    def add_to_queue(self):
        self.text_input_str = self.ids.my_text_input.text
        self.ids.my_text_input.text = ""

class SimpleYTConverterApp(App):
    pass

SimpleYTConverterApp().run()