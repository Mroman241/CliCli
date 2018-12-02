import kivy

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.graphics import *

class CliClicker(BoxLayout):

    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    def bg_change(self):
        #Change background according value set in radio buttons
        if self.blue:
            print('color changed to blue')
            with self.menuoptions.canvas:
                Color(rgba=(.7,.7,.9,1))
                Rectangle(pos = self.pos, size = self.size)
        elif self.red:
            print('color changed to red')
            with self.menuoptions.canvas:
                Color(rgba=(.9,.7,.7,1))
                Rectangle(pos = self.pos, size = self.size)
        elif self.green:
            print('color changed to green')
            with self.menuoptions.canvas:
                Color(rgba=(.7,.9,.7,1))
                Rectangle(pos = self.pos, size = self.size)

    def show_value(self, instance, value, box):
        self.value = box
        print(instance, box, self.value)
        print('blue', self.blue)
        print('red', self.red)
        print('green', self.green)
        
        

    def exit_app(self):
        #Exit the application and close the window
        pass

    def reset_score(self):
        #Take current score, divide it, add it to clicks and set it to 0
        pass

    def show_desc(self):
        pass

        #Get item description from array/dict, show it in label and set
        #the buy upgrade button to this item

    
    def buy_upgrade(self):
        pass
        #Take value Buy 1 -> value 1, Buy 10 -> value 10, buy input -> value = TextInput

        #Add specific bonus to clicks

    def click(self):
        pass

        #Get all added values and add it to score

        #Spawn a label at random coords

class MainApp(App):

    def build(self):
        return CliClicker()

app = MainApp()
app.run()
