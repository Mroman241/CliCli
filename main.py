import kivy

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty

class CliClicker(BoxLayout):

    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)


class MainApp(App):

    def build(self):
        return CliClicker()

app = MainApp()
app.run()
