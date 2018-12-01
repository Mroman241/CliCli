import kivy

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class CliClicker(BoxLayout):
    pass

class MainApp(App):

    def build(self):
        return CliClicker()

app = MainApp()
app.run()
