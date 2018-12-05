import kivy

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.graphics import *
from random import randint, random
from time import *
from kivy.clock import Clock
from functools import partial


class CliClicker(BoxLayout):

    # CLICK TAB VARIABLES
    clicol = ObjectProperty()

    # MENU TAB VARIABLES
    blue = ObjectProperty(False)
    red = ObjectProperty(False)
    green = ObjectProperty(True)

    score = ObjectProperty()

    # RESET TAB VARIABLES
    reset_boost = ObjectProperty()
    reset_bonus = 0

    # UPGRADE TAB VARIABLES
    description = ObjectProperty()
    item_name = ObjectProperty()
    price = ObjectProperty()
    current_button = ''

    descriptions = {'Button power': 'Increases the power you put into the button click',
                    'Percent increase': 'Increases all gains by a certain percent',
                    'Button shine': 'Makes the button shinier! (Also gives you a bonus to your clicks if shiny buttons are not enough)',
                    'Auto click I': 'Gives you a click each second',
                    'Auto click II': 'Gives you ten clicks each second',
                    'Auto click III': 'Gives you hundred clicks each second',
                    'Auto click IV': 'Gives you all the clicks you will ever need (it gives you 1000 clicks per second)'}

    prices = {'Button power': 10,
              'Percent increase': 100,
              'Button shine': 100,
              'Auto click I': 10,
              'Auto click II': 100,
              'Auto click III': 1000,
              'Auto click IV': 10000, }

    upgrade_parameters = {'Button power': 0,
                          'Percent increase': 0,
                          'Button shine': 0,
                          'Auto click I': 0,
                          'Auto click II': 0,
                          'Auto click III': 0,
                          'Auto click IV': 0, }

    button_power = 0
    percent_increase = 0
    button_shine = 0
    auto_cc1 = 0
    auto_cc2 = 0
    auto_cc3 = 0
    auto_cc4 = 0

    def __init__(self):
        super(CliClicker, self).__init__()
        Clock.schedule_interval(self.update, 1)
        print('I have been updated')

    def bg_change(self):
        # Change background according value set in radio buttons
        if self.blue:
            print('color changed to blue')
            with self.menuoptions.canvas:
                print('Changing color')
                self.col = (.7, .7, .9, 1)
                # Rectangle(pos=self.pos, size=self.size)
        elif self.red:
            print('color changed to red')
            with self.menuoptions.canvas:
                print('Changing color')
                self.col = (.9, .7, .7, 1)
                # Rectangle(pos=self.pos, size=self.size)
        elif self.green:
            print('color changed to green')
            with self.menuoptions.canvas:
                print('Changing color')
                self.col = (.7, .9, .7, 1)
                # Rectangle(pos=self.pos, size=self.size)

    def exit_app(self):
        # Exit the application and close the window
        pass

    def reset_score(self):
        # Take current score, divide it, add it to clicks and set it to 0
        self.reset_bonus += self.reset_boost
        self.score = 0

    def show_desc(self, button_text):
        # Get item description from array/dict, show it in label
        self.description = self.descriptions[button_text]
        self.item_name = button_text
        self.price = self.prices[button_text]
        self.current_button = button_text

    def buy_upgrade(self, amount):
        # Take value Buy 1 -> value 1, Buy 10 -> value 10, buy input -> value = TextInput
        try:
            upgrade_amount = int(amount)
        except Exception:
            print('ERROR: Wrong value entered')
            return None
        print('Upgrading', self.current_button, 'by amount: ', upgrade_amount, 'of price:', self.prices[self.current_button], 'with score:', self.score)
        for i in range(upgrade_amount):
            if self.prices[self.current_button] < self.score:
                self.score -= self.prices[self.current_button]
                self.prices[self.current_button] = round(self.prices[self.current_button]*1.5, 2)
                self.price = self.prices[self.current_button]
                print('Upgrade bought')
                self.upgrade_parameters[self.current_button] += 1
                print('Upgraded parameter of:', self.current_button, 'to', self.upgrade_parameters[self.current_button])
                if self.current_button == 'Button shine':
                    for i in range(3):
                        self.clicol[i] += self.upgrade_parameters['Button shine'] * 0.05
                    print(self.clicol)

                    self.clicli.background_color = self.clicol
            else:
                print('ERROR: Not enough score')
        # Add specific bonus to clicks
        self.button_power = self.upgrade_parameters['Button power']
        self.percent_increase = self.upgrade_parameters['Percent increase']
        self.button_shine = self.upgrade_parameters['Button shine']
        self.auto_cc1 = self.upgrade_parameters['Auto click I']
        self.auto_cc2 = self.upgrade_parameters['Auto click II']
        self.auto_cc3 = self.upgrade_parameters['Auto click III']
        self.auto_cc4 = self.upgrade_parameters['Auto click IV']



    def click(self):
        print('I have been clicked, my bonus is:', (self.button_power+self.button_shine*0.5))
        # Add a random value as base score
        addition = round((randint(1, 100)/100) * (1 + self.reset_bonus) + (self.button_power+self.button_shine*0.5), 2)
        # Get all added values and add it to score
        self.score += round(addition, 1)+(round(addition, 1)*(0.05*self.percent_increase))
        # Spawn a label at random coords
        l = Label(size_hint=(None, None), pos_hint={"right": random(), "top": random()})
        self.clitab.add_widget(l)

        self.reset_boost = self.score * 0.01

    def update(self, _):
        self.score += (self.auto_cc1*1)+(self.auto_cc2*10)+(self.auto_cc3*100)+(self.auto_cc4*1000) + (((self.auto_cc1*1)+(self.auto_cc2*10)+(self.auto_cc3*100)+(self.auto_cc4*1000))*(0.05*self.percent_increase))




class MainApp(App):

    def build(self):
        return CliClicker()


app = MainApp()
app.run()
