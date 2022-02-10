from kivy.app import App
from ytconvert import test
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    def on_button_click(self):
        print(test())

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()