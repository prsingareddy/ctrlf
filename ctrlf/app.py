import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Button

class HelloKivy(App):

    def build(self):
        return Button(text="Hello Kivy")

hellokivy = HelloKivy()
hellokivy.run()
cn